# Generated by Django 5.1.1 on 2024-10-05 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0006_news_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='name',
        ),
    ]