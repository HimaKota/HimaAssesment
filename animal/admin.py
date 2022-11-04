from django.contrib import admin
from .models import Breed, Animal, UserEntry

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    list_filter = ('name',)

class BreedAdmin(admin.ModelAdmin):
	list_display = ('animal','breed') 


class UserEntryAdmin(admin.ModelAdmin):
	list_display = ('animal','breed','date')
    
admin.site.register(Breed,BreedAdmin)
admin.site.register(Animal,AnimalAdmin)
admin.site.register(UserEntry,UserEntryAdmin)