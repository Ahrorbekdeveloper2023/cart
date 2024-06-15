from django.db import models

class Cotegory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='product_image', null=True)
    cotegory = models.ForeignKey(Cotegory, on_delete=models.CASCADE, related_name='products')
    is_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    

class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}"

    @property
    def totle_price(self):
        return self.product.price * self.quantity