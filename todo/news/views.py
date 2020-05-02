from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    return render(request, 'news.html')
# return HttpResponse('news')


def home(request):
    return render(request, 'index.html')
    # return HttpResponse('Home')


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('Contact')
