from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<div class = "kutu" ><h3 style="color:blue;">Hello World</h3></div>')
