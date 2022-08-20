from atexit import register
from inspect import CORO_SUSPENDED
from sqlite3 import Cursor
from django.contrib import admin

from ebanxSearch.models import *
from ebanxSearch.models.Course import Course
from .models import *
from ebanxSearch.forms import DepartmentListForm
from django.contrib.admin.views.main import ChangeList

#https://medium.com/@yprashant158/how-to-edit-manytomanyfield-in-django-admin-list-display-page-4687ec428639#

class ProfileAdminList(ChangeList):
    def __init__(self, request, model, list_display,
            list_display_links, list_filter, date_hierarchy,
            search_fields, list_select_related, list_per_page,
            list_max_show_all, list_editable, model_admin, sortable_by, search_help_text,
        ):    
        
        super(ProfileAdminList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, 
            model_admin,sortable_by, search_help_text,
        )

        # these need to be defined here, and not in MovieAdmin
        self.search_fields = ('user__username',)
        self.readonly_fields = ('user',)
        self.exclude = ('created_at', 'updated_at')
        self.date_hierarchy = 'created_at'
        self.list_display = ('user', 'role', 'departaments')
        self.list_display_links = ('user', 'role',)
        
        self.empty_value_display = '----'
        self.list_filter = ('user__is_active', 'role')
        self.fieldsets = (
            ('Usuário', {
                'fields': ('user','image')
            }),
            ('Função', {
                'fields': ('role',)
            }),
            
        )

class ProfileAdmin(admin.ModelAdmin):

    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)

    def get_changelist(self, request, **kwargs):
        return ProfileAdminList

    def get_changelist_form(self, request, **kwargs):
        return DepartmentListForm

    def departaments(self, obj):
        if obj.department.all():
            return list(obj.department.all().values_list('name', flat=True))
        else:
            return '-'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department)
admin.site.register(Course)

# Register your models here.
