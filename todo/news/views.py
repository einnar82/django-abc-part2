from django.shortcuts import HttpResponse, get_list_or_404, redirect, render
from .models import News, User
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
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


def signup(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'pages/signup.html', context)


def register(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        register = User.objects.create(**form.cleaned_data)
        messages.success(request, 'Successfully registered!')
        return redirect('signup')
