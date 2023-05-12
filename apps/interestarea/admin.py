from django.contrib import admin

from .models import InterestArea

class InterestAreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'uuid', 'create_date')
    

admin.site.register(InterestArea,InterestAreaAdmin)

