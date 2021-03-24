from .models import Platform, Topic

def get_platforms_to_context(request):
  platforms = Platform.objects.all()
  topics = Topic.objects.all()
  return {'platforms': platforms, 'topics' : topics}