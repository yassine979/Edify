from django.shortcuts import render
from django.urls import path
# Create your views here.

def index(request):
    return render(request,'pages/index.html', {})

def about(request):
    return render(request,'pages/about.html', {})

def contact(request):
    return render(request,'pages/contact.html', {})

def courses(request):
    return render(request,'pages/courses.html', {})

def team(request):  
    return render(request,'pages/team.html', {})

def testimonials(request):
    return render(request,'pages/testimonial.html', {})

def error_404(request):
    return render(request, 'pages/404.html')