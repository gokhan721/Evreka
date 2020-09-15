from django.contrib import admin
from navigation_record import models
# Register your models here.

admin.site.register(models.Vehicle)
admin.site.register(models.NavigationRecord)
