from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True,null = True)
    price = models.DecimalField(max_digits=1000,decimal_places=2,default=12.99)
    
    @property
    def sales_price(self):
        return "%.2f" %(float(self.price) * 0.9)
    
    def my_discount(self):
        return "%.3f" %(float(self.price)* 0.5)
