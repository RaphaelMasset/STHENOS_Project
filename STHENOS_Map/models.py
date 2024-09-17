from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class LieuxInteret (models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(max_length=100)

    def __str__(self):
        return self.name 
    
class LimiteDepFr(models.Model):
    id = models.AutoField(primary_key=True)
    code_insee = models.CharField(max_length=80)
    nom = models.CharField(max_length=80)
    nuts3 = models.CharField(max_length=80, null=True, blank=True)
    wikipedia = models.CharField(max_length=80)
    wikidata = models.CharField(max_length=80)
    surf_ha = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nom 
    
'''

class courbesDeNiveau(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    altitude = models.FloatField()
    nat_topo = models.CharField(max_length=7)
    importance = models.CharField(max_length=10)
    geom = models.MultiLineStringField(srid=4326)
    
    def __str__(self):
        return self.id


class LimiteCommunes(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    nom = models.CharField(max_length=80)
    nom_m = models.CharField(max_length=80)
    insee_com = models.CharField(max_length=80)
    statut = models.CharField(max_length=80)
    population = models.FloatField()
    insee_can = models.CharField(max_length=80)
    insee_arr = models.CharField(max_length=80)
    insee_dep = models.CharField(max_length=80)
    insee_reg = models.CharField(max_length=80)
    siren_epci = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.id


class limiteDepHerault(models.Model):
    id = models.AutoField(primary_key=True)
    code_insee = models.CharField(max_length=80)
    nom = models.CharField(max_length=80)
    nuts3 = models.CharField(max_length=80)
    wikipedia = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nom

class limiteEuropeCountries(models.Model):
    id = models.AutoField(primary_key=True)
    gid_0 = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)'''