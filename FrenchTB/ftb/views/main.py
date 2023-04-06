from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'index.html')
def index_old(request):
    return render(request, 'index_old.html')