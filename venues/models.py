from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50,blank=True,null=True,verbose_name=u'Categoria')

    def __unicode__(self):
        return self.category

class Cities(models.Model):
    city = models.CharField(max_length=25,blank=True,null=True,verbose_name=u'Ciudad')
    def __unicode__(self):
        return self.city

class States(models.Model):
    state = models.CharField(max_length=25,blank=True,null=True,verbose_name=u'Estado')
    def __unicode__(self):
        return self.state

class Venues(models.Model):
    fourSquareId = models.CharField(max_length=30,verbose_name=u'FourSquareId')
    name = models.CharField(max_length=45,verbose_name=u'Nombre')
    description = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Descripcion')
    url = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Sitio Web')
    url_image = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Foto')
    address = models.CharField(max_length=200,blank=True,null=True,verbose_name=u'Direccion')
    
    lat = models.CharField(max_length=25,verbose_name=u'Latitud')
    lng = models.CharField(max_length=25,verbose_name=u'Longitud')
    
    category = models.ForeignKey(Categories,blank=True,null=True)
    city = models.ForeignKey(Cities,blank=True,null=True)
    state = models.ForeignKey(States,blank=True,null=True)

    def __unicode__(self):
        return self.fourSquareId + ' ' + self.name

