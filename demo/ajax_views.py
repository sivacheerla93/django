from django.shortcuts import render, HttpResponse
from datetime import datetime


def ajax(request):
    return render(request, 'demo/ajax/ajax.html')


def today(request):
    now = datetime.now()
    return HttpResponse(now)
