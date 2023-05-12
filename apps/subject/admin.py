from django.contrib import admin

from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('description', 'uuid')

admin.site.register(Subject,SubjectAdmin)

