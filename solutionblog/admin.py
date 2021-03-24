from django.contrib import admin

from .models import Platform, Question, Language, Solution, Example, Topic

class ExampleInline(admin.StackedInline):
  model = Example
  extra = 0

class SolutionInline(admin.StackedInline):
  model = Solution
  extra = 0

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ExampleInline, SolutionInline]

admin.site.register(Platform)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Language)
admin.site.register(Topic)


