from .models import Platform

def get_platforms_to_context(request):
  platforms = Platform.objects.all()
  return {'platforms': platforms}