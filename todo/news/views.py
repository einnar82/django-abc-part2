from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    return render(request, 'pages/news.html')
# return HttpResponse('news')


def home(request):
    return render(request, 'pages/index.html')
    # return HttpResponse('Home')


def contact(request):
    return render(request, 'pages/contact.html')
    # return HttpResponse('Contact')
