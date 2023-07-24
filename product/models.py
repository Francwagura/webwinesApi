from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, null=False)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name

class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    country = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    size = models.IntegerField()
    abv = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    availability = models.BooleanField()
    shipment = models.DecimalField(default=0, decimal_places=2, max_digits=15)


    def __str__(self):
        return self.name