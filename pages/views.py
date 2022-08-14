from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('pages/index.html')
    context = { 'page_title' : 'Home | Uphomester' }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('pages/about.html')
    context = { 'page_title' : 'About Us | Uphomester' }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('pages/contact.html')
    context = { 'page_title' : 'Contact Us | Uphomester' }
    return HttpResponse(template.render(context, request))


def singup(request):
    template = loader.get_template('pages/signup.html')
    context = { 'page_title' : 'Sign up | Uphomester' }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('pages/login.html')
    context = { 'page_title' : 'Log in | Uphomester' }
    return HttpResponse(template.render(context, request))


def realtors(request):
    template = loader.get_template('pages/realtors.html')
    context = { 'page_title' : 'Agents | Uphomester' }
    return HttpResponse(template.render(context, request))


def listings(request):
    template = loader.get_template('pages/listings.html')
    context = { 'page_title' : 'Browse Listings | Uphomester' }
    return HttpResponse(template.render(context, request))