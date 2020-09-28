from django.contrib import admin
from travel.models import Destination, Traveller

# Register your models here.
# Model of Homepage
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img', 'desc', 'price']

admin.site.register(Destination, DestinationAdmin)

 # Model of Travellers
class TravellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'gender', 'image', 'email']

admin.site.register(Traveller, TravellerAdmin)
