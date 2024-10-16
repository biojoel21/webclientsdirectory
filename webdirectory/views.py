from django.shortcuts import render
from .models import Client, NewsFeed # type: ignore

# Create your views here.
def index(request):
    clients = Client.objects.all()
    news = NewsFeed.objects.all()
    return render(request, 'webdirectory/index.html', {'clients': clients, 'news': news})