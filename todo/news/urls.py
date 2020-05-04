from django.urls import path
from .views import news, home, contact, filter
urlpatterns = [
    path('news/', news, name='news'),
    path('news/<int:year>/', filter, name='filter'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
]
