from atexit import register
from inspect import CORO_SUSPENDED
from sqlite3 import Cursor
from django.contrib import admin

from ebanxSearch.models import *
from ebanxSearch.models.Course import Course
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    exclude = ('created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_display = ('user', 'role','departmentsList',)
    list_display_links = ('user', 'role',)
    empty_value_display = '----'
    list_filter = ('user__is_active', 'role')
    fieldsets = (
        ('Usuário', {
            'fields': ('user','image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        
    )
 
    def departmentsList(self, obj):
        return [i.name for i in obj.department.all()]

    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department)
admin.site.register(Course)

# Register your models here.
