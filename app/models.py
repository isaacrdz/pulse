from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)
    
    def __unicode__(self):
        return self.titulo


class Enlace(models.Model):
    titulo = models.CharField(max_length = 140)
    enlace = models.URLField()
    votos = models.IntegerField(default = 0)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s -  %s" % (self.titulo,self.enlace)

    def mis_votos_en_imagen_rosada(self):
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%d+votos' % self.votos

    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True

class Agregador(models.Model):
    titulo = models.CharField(max_length=140)
    enlaces = models.ManyToManyField(Enlace) 
