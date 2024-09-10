from django.shortcuts import render
from django.contrib.auth.models import User
from volantapp.models import Product,Color,Size,CartItem,Order,UserCart,ClientPersonalInfo
from volantapp.serializer import ProductSerializer,SizeSerializer,ColorSerializer,CartSerializer,RegisterSerializer,LoginSerializer,OrderSerializer, UserCartSerializer,ClientSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from google.auth.transport import requests as google_requests
from google.oauth2 import id_token


class GoogleAuthView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        if not username or not email:
            return Response({'error': 'Username and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create the user based on the provided email
        user, created = User.objects.get_or_create(email=email, defaults={'username': username})

        # If the user was just created, you can assign the username or handle further logic here
        if created:
            user.username = username
            user.save()

        # Generate or return the authentication token
        auth_token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': auth_token.key}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset=Size.objects.all()
    serializer_class=SizeSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset=Color.objects.all()
    serializer_class=ColorSerializer


class ProductFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Product.CATEGORY_CHOICES)
    size = django_filters.CharFilter(method='filter_by_size')
    color = django_filters.CharFilter(method='filter_by_color')
    sub_category = django_filters.ChoiceFilter(choices=Product.SUB_CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = ['category', 'sub_category']

    def filter_by_size(self, queryset, name, value):
        return queryset.filter(sizes__size=value)
    
    def filter_by_color(self ,queryset, name, value):
        return queryset.filter(colors__color=value)

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend]
    
class UserCartViewSet(viewsets.ModelViewSet):
    queryset = UserCart.objects.all()
    serializer_class = UserCartSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('user')
        
        user = User.objects.get(username=username)
        # return UserCart.objects.filter(user=user)
        cart = UserCart.objects.get(user=user)
        return CartItem.objects.filter(cart=cart)
    
        
        
class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('user')
        user = User.objects.get(username=username)
        
        # Get the user's cart
        user_cart = UserCart.objects.get(user=user)
        
        # Return all Cart items associated with the user's cart
        return CartItem.objects.filter(cart=user_cart)
    
    
    def delete(self, request, *args, **kwargs):
        try:
            product_id = request.query_params.get('id')
            username = request.query_params.get('user')
            user = User.objects.get(username=username)
            cart = UserCart.objects.get(user=user)

            if not product_id:
                return Response({"error": "Product ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)

        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Log the exception for debugging
            return Response({"error": "Internal server error: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)


# class CartViewSet(viewsets.ViewSet):
    
#     def list(self, request,*args, **kwargs):
#         if not request.user.is_authenticated:
#             return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
#         cart_items = Cart.objects.filter(user=request.user)
#         serializer = CartSerializer(cart_items, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=['post'])
#     def add_to_cart(self, request):
#         if not request.user.is_authenticated:
#             return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
#         product_id = request.data.get('product_id')
#         product = Product.objects.get(id=product_id)

#         cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)


#         serializer = CartSerializer(cart_item)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     @action(detail=False, methods=['post'])
#     def remove_from_cart(self, request):
#         if not request.user.is_authenticated:
#             return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
#         product_id = request.data.get('product_id')
#         cart_item = Cart.objects.get(user=request.user, product_id=product_id)
#         cart_item.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)









class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Order.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientPersonalInfo.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.query_params.get('user')
        user_id = User.objects.get(username = user) 
        if user:
            data = ClientPersonalInfo.objects.filter(user=user_id)
            return data

