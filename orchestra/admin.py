from .models import Orchestra
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class OrchestraAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Orchestra info'), {'fields': ('orchestra_name', 'email', 'admin_users', 'orchestra_type', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel', 'url', 'photo')}),
    )
    list_display = ('get_full_name', 'email', 'orchestra_type', 'prefecture', 'address', 'date_joined',)
    search_fields = ('orchestra_name', 'orchestra_name_kana', 'orchestra_type', 'email', 'prefecture', 'address',)
    ordering = ('date_joined',)

admin.site.register(Orchestra, OrchestraAdmin)
