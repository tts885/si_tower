from django.contrib import admin
from apps.pms.models.Work import Work
from import_export.admin import ImportExportModelAdmin
from reversion.admin import VersionAdmin

# Register your models here.
@admin.register(Work)
class WorkAdmin(ImportExportModelAdmin,VersionAdmin):

    list_display = ('id',  'name', 'status')

    list_display_links = ('id', 'name', 'status')

    