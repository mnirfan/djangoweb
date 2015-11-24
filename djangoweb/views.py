from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse('Hello World')

def home_page(request):
    html = """
        <!DOCTYPE html>
        <head>
            <title>Django test</title>
        </head>
        <body>
            <h1>Getting Started with Django</h1>
            <p>today i'm gonna learn Django beause it uses Python</p>
        </body>
    """
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':next_time})
