from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome in project: Northwind Database")

def about(request):
    return HttpResponse("Project for subject databases. Implentation Northwind database using Django and PostgreSQL")
