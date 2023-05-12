from django.contrib import admin

from .models import Category, Subject


class CategoryAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)
admin.site.register(Subject,SubjectAdmin)