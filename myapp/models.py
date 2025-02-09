from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=255,null=False,blank=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    def __str__(self):
        return self.name

class Contact3(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=255,null=False,blank=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    confirm_password = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name

class Nav(models.Model):
    img = models.CharField(max_length=100,null=True)
    texts = models.EmailField(max_length=255,null=True)
    s_texts = models.EmailField(max_length=255,null=True)
    
    
    def __str__(self):
        return self.img