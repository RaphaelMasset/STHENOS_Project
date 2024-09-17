from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin  # Ensure correct import
from .models import LieuxInteret, LimiteDepFr#, courbesDeNiveau, LimiteCommunes, limiteDepHerault, limiteEuropeCountries


# Register your models here.

class LieuxInteretAdmin(LeafletGeoAdmin):
    pass
    #list_display =['name', 'location']

class LimiteDepFrAdmin(LeafletGeoAdmin):
    pass
    list_display =['nom', 'code_insee']
    ordering = ['nom']


admin.site.register(LieuxInteret, LieuxInteretAdmin)
admin.site.register(LimiteDepFr, LimiteDepFrAdmin)
'''
class CourbesNivAdmin(LeafletGeoAdmin):
    #pass
    list_display =['altitude']

class LimitesCommunesAdmin(LeafletGeoAdmin):
    #pass
    list_display =['nom']

class LimitesHeraultAdmin(LeafletGeoAdmin):
    #pass
    list_display =['nom']

class LimiteEuropeCountriesAdmin(LeafletGeoAdmin):
    #pass
    list_display =['country']

'''

'''admin.site.register(courbesDeNiveau, CourbesNivAdmin)
admin.site.register(LimiteCommunes, LimitesCommunesAdmin)
admin.site.register(limiteDepHerault, LimitesHeraultAdmin)
admin.site.register(limiteEuropeCountries, LimiteEuropeCountriesAdmin)'''