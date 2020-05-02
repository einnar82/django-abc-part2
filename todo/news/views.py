from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    return render(request, 'news.html', {'title': 'News'})
# return HttpResponse('news')


def home(request):
    return render(request, 'index.html', {'title': 'Home'})
    # return HttpResponse('Home')


def contact(request):
    return render(request, 'contact.html', {'title': 'Contact'})
    # return HttpResponse('Contact')
