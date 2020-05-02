from django.urls import path
from .views import news, home, contact
urlpatterns = [
    path('news/', news, name='news'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
]
