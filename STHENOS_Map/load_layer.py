#this file is used to load the data into the DB
import os
from django.contrib.gis.utils import LayerMapping
from .models import LimiteDepFr#, courbesDeNiveau, LimiteCommunes, limiteDepHerault, limiteEuropeCountries
# Auto-generated `LayerMapping` dictionary for courbesDeNiveau model
courbesdeniveau_mapping = {
    'id': 'ID',
    'altitude': 'ALTITUDE',
    'nat_topo': 'NAT_TOPO',
    'importance': 'IMPORTANCE',
    'geom': 'MULTILINESTRING',
} #the firls of the shapefile are in caps here

# Auto-generated `LayerMapping` dictionary for LimiteCommunes model
limitecommunes_mapping = {
    'id': 'ID',
    'nom': 'NOM',
    'nom_m': 'NOM_M',
    'insee_com': 'INSEE_COM',
    'statut': 'STATUT',
    'population': 'POPULATION',
    'insee_can': 'INSEE_CAN',
    'insee_arr': 'INSEE_ARR',
    'insee_dep': 'INSEE_DEP',
    'insee_reg': 'INSEE_REG',
    'siren_epci': 'SIREN_EPCI',
    'type': 'TYPE',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for limiteEuropeCountries model
limiteeuropecountries_mapping = {
    'gid_0': 'GID_0',
    'country': 'COUNTRY',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for limiteDepHerault model
limitedepherault_mapping = {
    'code_insee': 'code_insee',
    'nom': 'nom',
    'nuts3': 'nuts3',
    'wikipedia': 'wikipedia',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for LimiteDepFr model
limitedepfr_mapping = {
    'code_insee': 'code_insee',
    'nom': 'nom',
    'nuts3': 'nuts3',
    'wikipedia': 'wikipedia',
    'wikidata': 'wikidata',
    'surf_ha': 'surf_ha',
    'geom': 'MULTIPOLYGON',
}


#courbes_niveau_shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/CourbeNiveauLambert93/COURBE_0600_6880.shp'))
limites_dep_fr_shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/gisData/departements-20170102-shp/departements-20170102.shp'))
#limites_communes_shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/ContourCommunesWGS83/COMMUNE_FRMETDROM.shp'))
#limites_dep_herault_shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/departement-34/admin-departement.shp'))
#limites_europe_countries_shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/euroCountries/Europe_merged.shp'))

#os.path.dirname(__file__)  is the path to the directory where this script is located

def loadLimitDepFr(verbose=True):
    lm = LayerMapping(LimiteDepFr, limites_dep_fr_shp_path, limitedepfr_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


'''
def loadCourbeNiv(verbose=True):
    lm = LayerMapping(courbesDeNiveau, courbes_niveau_shp_path, courbesdeniveau_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runLimitesCommunes(verbose=True):
    lm = LayerMapping(LimiteCommunes, limites_communes_shp_path, limitecommunes_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runLimitesDepHerault(verbose=True):
    lm = LayerMapping(limiteDepHerault, limites_dep_herault_shp_path, limitedepherault_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runLimitesEuropeCountries(verbose=True):
    lm = LayerMapping(limiteEuropeCountries, limites_europe_countries_shp_path, limiteeuropecountries_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)'''