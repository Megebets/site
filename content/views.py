from django.shortcuts import render
from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/main.html', {'images': images})
