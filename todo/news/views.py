from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    return HttpResponse('news')


def home(request):
    return HttpResponse('Home')


def contact(request):
    return HttpResponse('Contact')
