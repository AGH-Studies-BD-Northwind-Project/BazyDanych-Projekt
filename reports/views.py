from django.http import HttpResponse
from django.shortcuts import render

def reports(request):
    return HttpResponse("App for reports- To Do")