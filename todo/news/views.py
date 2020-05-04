from django.shortcuts import HttpResponse, get_list_or_404, render
from .models import News

# Create your views here.


def news(request):
    context = {
        "news": News.objects.get(id=1)
    }
    return render(request, 'pages/news.html', context)


def filter(request, year):

    context = {
        "year": year,
        # "news": News.objects.filter(pub_date__year=year)
        "news": get_list_or_404(News, pub_date__year=year)
    }
    return render(request, 'pages/filter.html', context)


def home(request):
    context = {
        "name": "John Doe"
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    return render(request, 'pages/contact.html')
