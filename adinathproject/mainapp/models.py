from django.db import models

# Create your models here.


class Carousel(models.Model):
    image=models.ImageField(upload_to='carousel/')

class Category(models.Model):
    category_name=models.CharField(max_length=2000)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    customizationchoices=[
        ('Yes','Yes'),
        ('No','No')
    ]
    product_code=models.CharField(max_length=100)
    product_name=models.CharField(max_length=2000)
    product_description=models.TextField()
    product_old_prize=models.PositiveIntegerField()
    product_prize=models.PositiveIntegerField()
    product_min_quantity=models.PositiveIntegerField(null=True,blank=True)
    product_customization=models.CharField(max_length=5,choices=customizationchoices,null=True)
    productimage_1=models.ImageField()
    productimage_2=models.ImageField(null=True,blank=True)
    productimage_3=models.ImageField(null=True,blank=True)
    productimage_4=models.ImageField(null=True,blank=True)
    productimage_5=models.ImageField(null=True,blank=True)
    productimage_6=models.ImageField(null=True,blank=True)
    productimage_7=models.ImageField(null=True,blank=True)
    productimage_8=models.ImageField(null=True,blank=True)
    productimage_9=models.ImageField(null=True,blank=True)
    productimage_10=models.ImageField(null=True,blank=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_sub_category=models.CharField(max_length=200)

    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=256)
    customer_email=models.EmailField()
    customer_number=models.CharField(max_length=10)
    company_name=models.CharField(max_length=300,null=True)
    customer_address=models.TextField(null=True,blank=True)
    order_completed=models.BooleanField()

    def __str__(self):
        return self.customer_name
