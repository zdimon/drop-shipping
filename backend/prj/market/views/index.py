from django.shortcuts import render

def index(request,slug='main'):
    return render(request,'index.html')

