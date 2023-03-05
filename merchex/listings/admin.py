from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year_formed", "genre")

admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "type", "band")

admin.site.register(Listing, ListingAdmin)
