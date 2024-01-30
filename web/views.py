from django.shortcuts import render
from django.core.serializers import serialize


def index(request):
  return render(request, 'index.html', { })

def about(request):
  return render(request, 'about.html', { })

def contact(request):
  return render(request, 'contact.html', { })