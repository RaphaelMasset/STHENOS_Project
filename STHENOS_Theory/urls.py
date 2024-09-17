from django.urls import include, path
from . import views

urlpatterns = [   
    path("theory/", views.theory, name="theory"),   
    path("links/", views.links, name="links"),   
    path("contact/", views.contact, name="contact"), 
]
