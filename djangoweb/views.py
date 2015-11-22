from django.http import HttpResponse, Http404
from django.template import Template, Context
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

def current_datetime(response):
    now = datetime.datetime.now()
    t = Template("""
        <!DOCTYPE html>
        <head>
            <title>Django test</title>
        </head>
        <body>
            <h1>Getting Started with Django</h1>
            <p>It is now {{ current_date }}</p>
        </body>
    """)
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    t = Template("""
         <!DOCTYPE html>
        <head>
            <title>Django test</title>
        </head>
        <body>
            <h1>Getting Started with Django</h1>
            <p>It is now {{ current_date }} in UTC+{{ timezone }}</p>
        </body>
    """)
    html = t.render(Context({'current_date':dt, 'timezone':offset}))
    return HttpResponse(html)

