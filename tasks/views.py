from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome To The Taks Management System</h1>")

def contact(request):
    return HttpResponse("<h2>This is Contact Page!!</h2>")

def blog(request):
    return HttpResponse("<h2>This is Blog Page!!</h2><p>This is a blog post.</p>")

def show_task(request):
    return HttpResponse("<h1>This is Task Page!</h2>")