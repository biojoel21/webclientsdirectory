from django.db import models

# Create your models here.
class Client (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    building = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class NewsFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)
    active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title