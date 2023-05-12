from django.contrib import admin

from .models import InterestArea

class InterestAreaAdmin(admin.ModelAdmin):
    pass

admin.site.register(InterestArea,InterestAreaAdmin)

