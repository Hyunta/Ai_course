from django.shortcuts import render

def register(request) :
    return render (request, 'register.html')

def read(request) :
    return render (request, 'read.html')

def list(request) :
    return render (request, 'list.html')

def delete(request) :
    return render (request, 'delete.html')

def modify(request) :
    return render (request, 'modify.html')