# Generated by Django 3.1.7 on 2021-03-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutionblog', '0011_auto_20210320_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('questions', models.ManyToManyField(to='solutionblog.Question')),
            ],
        ),
    ]
