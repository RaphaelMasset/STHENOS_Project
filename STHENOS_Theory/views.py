from django.http import HttpResponse
from django.shortcuts import render
import json, os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles import finders

# Create your views here.
def theory(request):
    json_file_path = finders.find('training.json')
    
    # Load the JSON data
    with open(json_file_path, 'r') as json_file:
        book_data = json.load(json_file)

    
    # Prepare data for template
    context = {
        'book_data': book_data,
        'current_page': 'theory'
    }
    
    return render(request, "theory.html", context)

def links(request):
     context = {'current_page': 'links'}
     return render (request,"links.html", context)

def contact(request):
    context = {'current_page': 'contact'}
    return render (request,"contact.html", context)