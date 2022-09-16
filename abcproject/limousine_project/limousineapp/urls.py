from . import views
from django.urls import path

app_name = 'limousineapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('bahrain/',views.bahrain,name='bahrain'),
    path('saudi/',views.saudi,name='saudi'),
    path('reviews/',views.review,name='reviews'),
    path('contact/', views.contact, name='contact'),

]
