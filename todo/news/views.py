from django.shortcuts import render, HttpResponse

# Create your views here.


def news(request):
    context = {
        "tech_stacks": ["Python", "PHP", "Node.js"]
    }
    return render(request, 'pages/news.html', context)
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
