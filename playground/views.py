from django.shortcuts import render
from django.http import HttpResponse
#takes request and gives response
#request handler

def landing_page(request):
    return render(request, "store/index.html")