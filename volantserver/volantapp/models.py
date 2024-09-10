from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES=[
        ('ladies','ladies'),
        ('gents','gents'),
        ('boys','boys'),
        ('girls','girls'),
        ('kids','kids')
    ]
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    SUB_CATEGORY_CHOICES=[
        ('sandals','sandals'),
        ('slipper','slipper'),
        ('flipflops','flipflops'),
        ('casualshoes','casualshoes'),
        ('flatshoes','flatshoes'),
        ('schooledition','schooledition'),
        ('shoes','shoes')
    ]
    sub_cateory = models.CharField(max_length=50,choices=SUB_CATEGORY_CHOICES)
    new_arrival = models.BooleanField(default=False)
    handmade_and_fastive = models.BooleanField(default=False)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="product_images")
    available=models.BooleanField(default=True)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    offer_percentage = models.CharField(max_length=100,blank=True,null=True)
    offer_is_available  = models.BooleanField(default=False)
    quantity = models.CharField(max_length=100,blank=True,null=True,default=1)

    def __str__(self):
        return self.name

class Size(models.Model):
    product=models.ForeignKey(Product,related_name='sizes',on_delete=models.CASCADE)
    size=models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    offer_percentage = models.CharField(max_length=100,blank=True,null=True)
    offer_is_available  = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} - {self.size}'


class Color(models.Model):
    product=models.ForeignKey(Product,related_name='colors',on_delete=models.CASCADE)
    colors=(
        ('Black','Black'),
        ('Blue','Blue'),
        ('Brown','Brown'),
        ('Camel','Camel'),
        ('Cherry','Cherry'),
        ('Gold','Gold'),
        ('Grape','Grape'),
        ('Green','Green'),
        ('Grey','Grey'),
        ('Maroon','Maroon'),
        ('Mehandi','Mehandi'),
        ('Navy','Navy'),
        ('Olive','Olive'),
        ('Peach','Peach'),
        ('Peacock','Peacock'),
        ('Pink','Pink'),
        ('Purple','Purple'),
        ('Tan','Tan'),
        ('Violet','Violet'),
        ('White','White'),
        ('Wine','Wine'),
        ('Yellow','Yellow'),
        ('sky blue','sky blue'),
        ('fblack','fblack'),
        ('Lemon','Lemon')
    )
    product_color=models.CharField(max_length=100,choices=colors)
    image=models.ImageField(upload_to="product_images_colors")

    def __str__(self):
        return f'{self.product.name} - {self.product_color}'

class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Product, through='CartItem')
    color = models.ManyToManyField(Color, through='CartItem')
    size = models.ManyToManyField(Size, through='CartItem')
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}\'s cart'


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} in {self.cart.user.username}\'s cart'



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    ORDER_STATUS_CHOICES = [
        ('order-placed', 'Order Placed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('user', 'product', 'color', 'size', 'status')  # Ensures uniqueness

    def __str__(self):
        return f"Order {self.id} - User: {self.user.username} - Product: {self.product.name}"



class ClientPersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileIphoto = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name =  models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=225, null=True,blank=True)
    email = models.EmailField( null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    landmark=models.CharField(max_length=200,null=True,blank=True)
    pincode=models.TextField(max_length=100,null=True,blank=True)
    streetaddress=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.streetaddress}'


