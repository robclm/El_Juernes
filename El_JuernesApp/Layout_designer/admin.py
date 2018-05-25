from .models import *
from django.contrib import admin

class PublishedAdmin(admin.ModelAdmin):
    readonly_fields = ('publishedtime', )

admin.site.register(Published_Article, PublishedAdmin)