from django.contrib import admin
from .models import News, SportsNews, User

# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(User)
