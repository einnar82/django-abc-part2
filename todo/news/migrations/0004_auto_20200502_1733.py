# Generated by Django 3.0.5 on 2020-05-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_sportsnews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
        migrations.AlterModelOptions(
            name='sportsnews',
            options={'verbose_name_plural': 'sports_news'},
        ),
    ]