from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")

def about(request):
    return HttpResponse("Project for subject databases. Implentation Northwind database using Django and PostgreSQL")
