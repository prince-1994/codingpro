# Generated by Django 3.1.7 on 2021-03-20 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutionblog', '0007_question_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='platform',
        ),
    ]