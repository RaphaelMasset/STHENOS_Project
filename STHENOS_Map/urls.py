from django.urls import include, path
from . import views


urlpatterns = [   
    path("", views.map, name="map"),
    path("limiteDepFr", views.limiteDepFrDataSet, name="limiteDepFr"),      
    path("lieuxInteret", views.lieuxInteretDataSet, name="lieuxInteret"),      
]
