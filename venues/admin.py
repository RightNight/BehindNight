from django.contrib import admin
from . import models

admin.site.register(models.Venue)
admin.site.register(models.Category)
admin.site.register(models.City)
admin.site.register(models.State)

admin.site.register(models.User)
admin.site.register(models.WantToGo)
admin.site.register(models.NowHere)


