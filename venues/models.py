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
#	FOREIGN KEY CATEGORIES

	def __unicode__(self):
        return self.fourSquareId + ' ' + self.name