from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('<h1> Hello Django  </h1>')

def index(request):
    return render (request , 'index.html')

# Create your views here.
