from django.db import models
from django.contrib.auth.models import User


class SiteSetupModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, null=True, blank=True)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    mobile_1 = models.CharField(max_length=20, null=True, blank=True)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class ContactModel(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20)


class GalleryModel(models.Model):
    image = models.FileField(upload_to='image/gallery')


