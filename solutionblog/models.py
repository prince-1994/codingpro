from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import Q

class Platform(models.Model):
  name = models.CharField(max_length=50)
  url = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Topic(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Question(models.Model):
  name = models.CharField(max_length=300)
  text = models.TextField()
  platform = models.ForeignKey(Platform, null=True,blank=True, related_name='questions', on_delete=CASCADE)
  topic = models.ManyToManyField(Topic, blank=True)
  def __str__(self):
    return self.name

class Example(models.Model):
  input = models.TextField()
  output = models.TextField()
  question = models.ForeignKey(Question, related_name='examples', on_delete=CASCADE)

class Language(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Solution(models.Model):
  language = models.ForeignKey(Language, related_name='solutions', on_delete=CASCADE)
  question = models.ForeignKey(Question, related_name='solutions', on_delete=CASCADE)
  code = models.TextField()


