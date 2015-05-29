from django.db import models

# Create your models here.

class Venues(models.Model):
	fourSquareId = models.CharField(max_length=30,verbose_name=u'FourSquareId')
	name = models.CharField(max_length=45,verbose_name=u'Nombre')
	description = models.CharField(max_length=250,verbose_name=u'Descripcion')
	url = models.CharField(max_length=250,verbose_name=u'Sitio Web')
	url_image = models.CharField(max_length=250,verbose_name=u'Foto')
	address = models.CharField(max_length=200,verbose_name=u'Direccion')
	
	lat = models.CharField(max_length=25,verbose_name=u'Latitud')
	lng = models.CharField(max_length=25,verbose_name=u'Longitud')
	category = models.ForeignKey(Categories)
	city = models.ForeignKey(Cities)
	state = models.ForeignKey(States)

	def __unicode__(self):
        return self.fourSquareId + ' ' + self.name

class Categories(models.model):
	category = models.CharField(max_length=50,verbose_name=u'Categoria')

	def __unicode__(self):
        return self.category

class Cities(models.model):
	city = models.CharField(max_length=25,verbose_name=u'Ciudad')
	def __unicode__(self):
        return self.city

class States(object):
	state = models.CharField(max_length=25,verbose_name=u'Estado')
	def __unicode__(self):
        return self.city