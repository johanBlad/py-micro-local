from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('yeheea')
    return HttpResponse('Hello there, from the Django app!')