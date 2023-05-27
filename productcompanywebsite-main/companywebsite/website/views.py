from django.shortcuts import render

def mainpage(request):
    return render(request,"index.html")

def contactus(request):
    return render(request,"contactus.html")

def people(request):
    return render(request,"people.html")

def products(request):
    return render(request,"products.html")