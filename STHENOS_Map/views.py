from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import LieuxInteret, LimiteDepFr#LimiteCommunes, Incidences, limiteDepHerault, limiteEuropeCountries

# Create your views here.
def map(request):
    context = {'current_page': 'map'}
    return render (request,"map.html", context)

# Create your views here.
def limiteDepFrDataSet (request):
    limiteDepHeraultJson = serialize('geojson', LimiteDepFr.objects.all()) 
    return HttpResponse(limiteDepHeraultJson, content_type='json')

def lieuxInteretDataSet (request):
    incidencesJson = serialize('geojson', LieuxInteret.objects.all()) 
    return HttpResponse(incidencesJson, content_type='json')

'''def limiteCommunesDataSet (request):
    limiteCommunesJson = serialize('geojson', LimiteCommunes.objects.all()) 
    return HttpResponse(limiteCommunesJson, content_type='json')

def limiteDepHeraultDataSet (request):
    limiteDepHeraultJson = serialize('geojson', limiteDepHerault.objects.all()) 
    return HttpResponse(limiteDepHeraultJson, content_type='json')



def limiteEuropeCountriesDataSet (request):
    limiteEuropeCoutnriesJson = serialize('geojson', limiteEuropeCountries.objects.all()) 
    return HttpResponse(limiteEuropeCoutnriesJson, content_type='json')'''