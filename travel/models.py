
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    price = models.IntegerField()


# Create your models here.
class Traveller(models.Model):
    firstname = models.CharField(max_length=50);
    lastname = models.CharField(max_length=50);
    gender = models.CharField(max_length=8);
    image = models.ImageField(upload_to='traveller_pics/');
    # dob = models.CharField(max_length=20);
    email = models.EmailField();
    password = models.CharField(max_length=50);
    createddate = models.CharField(max_length=20);
    logindate = models.CharField(max_length=20);
