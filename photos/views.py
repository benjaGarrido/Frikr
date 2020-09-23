from django.http import HttpResponse
from django.shortcuts import render

from photos.models import Photo


def home(request):
    # Configuramos la query
    photos = Photo.objects.all().order_by('-created_at')
    context = {
        # Django realiza ejecución perezosa de las querys
        'photos_list':photos[:5]
    }
    return render(request, 'photos/home.html', context)
