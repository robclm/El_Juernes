from django.contrib import admin


from Graphic_reporter.models import *


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('added', 'updated',)


admin.site.register(Image, ImageAdmin)
admin.site.register(Image_request)
