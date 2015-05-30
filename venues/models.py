from django.db import models

# Create your models here.
#blank=True,null=True volverlos NOT OBLIGATORY
class User(models.Model):
    faceBookId = models.CharField(max_length=200,verbose_name=u'FaceBookId')
    name = models.CharField(max_length=200,verbose_name=u'Nombre')
    def __unicode__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=50,blank=True,null=True,verbose_name=u'Categoria')
    def __unicode__(self):
        return self.category

class City(models.Model):
    city = models.CharField(max_length=25,blank=True,null=True,verbose_name=u'Ciudad')
    def __unicode__(self):
        return self.city

class State(models.Model):
    state = models.CharField(max_length=25,blank=True,null=True,verbose_name=u'Estado')
    def __unicode__(self):
        return self.state

class Venue(models.Model):
    fourSquareId = models.CharField(max_length=30,verbose_name=u'FourSquareId')
    name = models.CharField(max_length=45,verbose_name=u'Nombre')
    description = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Descripcion')
    url = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Sitio Web')
    url_image = models.CharField(max_length=250,blank=True,null=True,verbose_name=u'Foto')
    address = models.CharField(max_length=200,blank=True,null=True,verbose_name=u'Direccion')
    
    lat = models.CharField(max_length=25,verbose_name=u'Latitud')
    lng = models.CharField(max_length=25,verbose_name=u'Longitud')
    
    category = models.ForeignKey(Category,blank=True,null=True)
    city = models.ForeignKey(City,blank=True,null=True)
    state = models.ForeignKey(State,blank=True,null=True)
    visits = models.IntegerField(max_length=10,default=0)
    nowHere = models.IntegerField(max_length=10,default=0)

    def __unicode__(self):
        return self.fourSquareId + ' ' + self.name

class WantToGo(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    venue = models.ForeignKey(Venue)
    
    def __unicode__(self):
        return self.date + ' ' + self.user + ' a '+self.venue 

class NowHere(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    venue = models.ForeignKey(Venue)

    def __unicode__(self):
        return self.date + ' ' + self.user + ' esta en '+self.venue
