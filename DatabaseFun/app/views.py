"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import *;

def artists(request):
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>');
    artists = Artist.objects.all();
    return render_to_response('app/artists.html', { 'artists' : artists });

def artistdetails(request, id):
    #output = '<html><head><title>' + id
    #output += '</title></head><body><h1>' + id
    #output += '</h1></body></html>'
    #return HttpResponse(output);
    artist = Artist.objects.get(pk = id);
    return render_to_response('app/artistdetails.html', { 'artist' : artist});

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
