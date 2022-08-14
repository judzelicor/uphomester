from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'root'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('signup', views.singup, name ='signup'),
    path('login', views.login, name = 'login'),
    path('realtors', views.realtors, name = 'realtors'),
    path('listings', views.listings, name ='listings')
]