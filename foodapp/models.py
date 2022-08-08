from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=900, blank=True, null=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField()
    imageUrl = models.CharField(max_length=900, blank=True, null=True)
    isGlutenFree = models.BooleanField(default=False)
    isVegeterian = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    dishes = models.ManyToManyField(Dish)
    time = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=20)
        
    def __str__(self):
        return self.dishes.name + '-' + self.time