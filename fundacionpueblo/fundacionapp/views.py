from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.

def home(request):
    return render(request, 'fundacionapp/home.html'); 

def somos(request):
    return render(request, 'fundacionapp/somos.html'); 

def blog(request):
    return render(request, 'fundacionapp/blog.html'); 





 

