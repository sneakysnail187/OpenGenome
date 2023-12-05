from django.shortcuts import render
from django.http import HttpResponse

#functions for rendering the individual html pages 
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')