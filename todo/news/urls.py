from django.urls import path
from .views import news, home, contact, filter, signup, register, model_form, submit_form
urlpatterns = [
    path('news/', news, name='news'),
    path('news/<int:year>/', filter, name='filter'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
    path('model-form/', model_form, name='model_form'),
    path('submit-form/', submit_form, name='submit_form'),
]
