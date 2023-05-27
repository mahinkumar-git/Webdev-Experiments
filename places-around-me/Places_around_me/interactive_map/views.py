from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def Anna_Stadium(request):
    return render(request, "Anna_stadium.html")

def postoffice(request):
    return render(request, "postoffice.html")

def railway(request):
    return render(request, "railway.html")

def bridge(request):
    return render(request, "bridge.html")

def busstand(request):
    return render(request, "busstand.html")