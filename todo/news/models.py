from django.db import models

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
