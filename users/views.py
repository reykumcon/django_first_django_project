from django.shortcuts import render, HttpResponse

def new(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')

def index(request):
    return HttpResponse('placeholder to later display all the list of users')
