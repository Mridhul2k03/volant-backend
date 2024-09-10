from rest_framework import serializers
from django.contrib.auth.models import User
from volantapp.models import Color,Product,Size,CartItem,Order,UserCart,ClientPersonalInfo
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    size=SizeSerializer(many=True,read_only=True)
    color=ColorSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
    

class UserCartSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=UserCart
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        username = request.data.get('user')
        product_id = request.data.get('items')  # Assuming 'items' contains the product ID
        color = request.data.get('color')
        size = request.data.get('size')
        
        user = User.objects.get(username=username)

        # Get or create the UserCart for the user
        user_cart, created = UserCart.objects.get_or_create(user=user)
        
        # Get the product instance
        product = Product.objects.get(id=product_id)
        color_id = Color.objects.get(product_color = color,product = product_id)
        size_id = Size.objects.get(size=size,product = product)

        # Check if the Cart item exists
        cart_item, item_created = CartItem.objects.get_or_create(cart=user_cart, product=product,color = color_id,size = size_id)

        if not item_created:
            # If the item already exists, increase the quantity
            cart_item.quantity += 1
            cart_item.save()

        # Ensure the UserCart instance is returned
        return user_cart   
    

                 
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    # user = serializers.ReadOnlyField(source='user.username')
    # product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')   
        product = validated_data.get('product')
        cart = validated_data.get('cart')
        
        if CartItem.objects.filter(cart=cart, product=product).exists():
            raise serializers.ValidationError("Product already exists in the cart.")
        else:
            return CartItem.objects.create(product=product, cart=cart)

    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'added_at', 'color', 'size', 'status']
        
        

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = ClientPersonalInfo
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get('request')
        username = request.data.get('user') if request else None
        
        if not username:
            raise serializers.ValidationError("User field is required.")
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        return ClientPersonalInfo.objects.create(user=user, **validated_data)