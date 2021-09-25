from django.contrib import admin
from .models import Upload,OperatorEdge
# Register your models here.
# admin.site.register(Upload)
# @admin.register()
# date_hierarchy
class UploadAdminSettings(admin.ModelAdmin):
    search_fields= ('action',)
    list_filter = ('start_date',)
    ordering = ('-start_date',)
    list_display = ('id','action','start_date')



admin.site.register(Upload,UploadAdminSettings)
admin.site.register(OperatorEdge)





