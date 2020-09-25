from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return self.name


class Listings(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200,blank=True)
    address=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    state=models.CharField(max_length=200,blank=True)
    zipcode=models.IntegerField()
    price=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    bedrooms=models.IntegerField()
    bathroom=models.IntegerField()
    Sqft=models.IntegerField()
    Garage=models.IntegerField()
    main_photo=models.ImageField(blank=True)
    photo_1=models.ImageField(blank=True)
    photo_2=models.ImageField(blank=True)
    photo_3=models.ImageField(blank=True)
    photo_4=models.ImageField(blank=True)
    photo_5=models.ImageField(blank=True)
    photo_6=models.ImageField(blank=True)
    public=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    listing=models.CharField(max_length=200,null=True,blank=True)
    listing_id=models.IntegerField(null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(null=True)


