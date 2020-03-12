from django.db import models


# Create your models here.
class GetDB(models.Model):
    ip = models.CharField(max_length=68, blank=True, null=True, default="无")
    address = models.CharField(max_length=256, blank=True, null=True, default="无")
    data = models.DateTimeField(auto_now=True)


class PostDB(models.Model):
    ip = models.CharField(max_length=68, blank=True, null=True, default="无")
    address = models.CharField(max_length=256, blank=True, null=True, default="无")
    message = models.TextField(null=True, blank=True, default="无")
    file_name = models.CharField(max_length=128, blank=True, null=True, default="无")
    data = models.DateTimeField(auto_now=True)


class LoginUser(models.Model):
    ip = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True, default="无")
    data = models.DateTimeField(auto_now=True)
