from django.contrib import admin
from django.urls import path, include

# Register your models here.
from .models import Client, NewsFeed

admin.site.register(Client)
admin.site.register(NewsFeed)