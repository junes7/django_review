from django.contrib import admin
from .models import Musician, Album
# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    admin.site.register(Musician)
    admin.site.register(Album)
    
