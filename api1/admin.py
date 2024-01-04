from django.contrib import admin

from api1.models import Movie,collections
# Register your models here.

class Movieadmin(admin.ModelAdmin):
    list_display=("title","release_date","Description")
    search_fields=("title",)
admin.site.register(Movie,Movieadmin)

class colladmin(admin.ModelAdmin):
    list_display=("name","email","movie")
    list_filter=('movie',)
admin.site.register(collections,colladmin)