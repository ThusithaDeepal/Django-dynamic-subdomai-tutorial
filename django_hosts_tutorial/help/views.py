from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>this is help homepage</h1>')


def articles(request):
    return HttpResponse('<h1>this is help articles homepage</h1>')