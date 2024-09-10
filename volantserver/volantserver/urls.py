"""
URL configuration for volantserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from volantapp.views import ProductViewSet,SizeViewSet,ColorViewSet,CartViewSet,RegisterView,FilterViewSet,OrderViewSet,UserCartViewSet,UserAddressViewSet,GoogleAuthView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
router=DefaultRouter()

router.register(r'products',ProductViewSet,basename='products')
router.register(r'sizes',SizeViewSet,basename='sizes')
router.register(r'colors',ColorViewSet,basename='colors')
router.register(r'cart_view',CartViewSet,basename='cart_view')
router.register(r'user_address', UserAddressViewSet, basename='address')
router.register(r'filter',FilterViewSet,basename='filter')
router.register(r'order',OrderViewSet,basename='order')
router.register(r'user_cart',UserCartViewSet,basename='user_cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/register/', RegisterViewSet.as_view({'post': 'register'}), name='user-register'),
    # path('users/login/', RegisterViewSet.as_view({'post': 'login'}), name='user-login'),
    path('api/google-auth/', GoogleAuthView.as_view(), name='google-auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

