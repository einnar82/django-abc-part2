from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    return render(request, 'pages/news.html')
# return HttpResponse('news')


def home(request):
    context = {
        "name": "John Doe"
    }
    return render(request, 'pages/index.html', context)
    # return HttpResponse('Home')


def contact(request):
    return render(request, 'pages/contact.html')
    # return HttpResponse('Contact')
