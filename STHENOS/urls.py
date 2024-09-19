"""
URL configuration for STHENOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("STHENOS_Index.urls")),
   # path('<str:name>', include("STHENOS_Index.urls")),
    path('calculators/', include("STHENOS_Calculators.urls")),
    path('programs/', include("STHENOS_Programs.urls")),
    path('network/', include("STHENOS_Network.urls")),
    path('game/', include("STHENOS_Game.urls")),
    path('map/', include("STHENOS_Map.urls")),

    path('', include("STHENOS_Theory.urls")),
]

