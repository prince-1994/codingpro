# Generated by Django 3.1.7 on 2021-03-20 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutionblog', '0010_auto_20210320_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
