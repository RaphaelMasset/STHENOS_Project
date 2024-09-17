from django.urls import include, path
from . import views

urlpatterns = [   
    path("", views.programs, name="programs"),      
    #path("pdf/", views.generate_pdf_view, name="generate_pdf_view"),      
]

