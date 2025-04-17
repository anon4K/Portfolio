from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'section/home.html', {'projects': projects})
# Create your views here.
# def home(request):
#     return render(request, 'section/home.html')
