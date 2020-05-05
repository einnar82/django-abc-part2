from django.db import models
from django.utils import timezone

# Create your models here.


class News(models.Model):
    # By default table names created via migration makes a format like {app_name.model_name}
    # To override this behavior, simply override it via Metaclass
    class Meta:
        db_table = 'news'
        # change the pluralize behavior of model
        verbose_name_plural = 'news'

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author


class SportsNews(models.Model):
    class Meta:
        db_table = 'sports_news'
        # change the pluralize behavior of model
        verbose_name_plural = 'sports_news'

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class User(models.Model):
    class Meta:
        db_table = 'users'
        # change the pluralize behavior of model
        verbose_name_plural = 'users'

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username
