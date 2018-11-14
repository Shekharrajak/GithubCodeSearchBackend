from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
import requests
import json


def index(request):
    return HttpResponse('I am up!')

def searchCode(request):
    req = requests.get('https://api.github.com/users/shekharrajak')
    content = req.text
    return HttpResponse(content)
