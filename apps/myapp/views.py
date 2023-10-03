# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home page :)")


def contacts(request):
    return HttpResponse("<h1>You can call us: 000-555-222</h1>")
