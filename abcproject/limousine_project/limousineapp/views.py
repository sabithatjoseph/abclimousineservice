from django.shortcuts import render, redirect
from .models import findyourcar


# Create your views here.
def index(request):
    obj = findyourcar.objects.all()
    return render(request, 'index.html', {'car': obj})


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def bahrain(request):
    return render(request, 'bahrain.html')


def saudi(request):
    return render(request, 'saudi.html')


def review(request):

    return render(request, 'reviews.html')


def contact(request):
    return render(request, 'contact.html')
