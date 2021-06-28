from .models import Orchestra
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class OrchestraAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Orchestra info'), {'fields': ('orchestra_name', 'email', 'admin_users', 'orchestra_type1', 'orchestra_type2', 'birthday', 'postal_code', 'prefecture', 'address', 'building', 'tel', 'url', 'photo')}),
    )
    list_display = ('get_full_name', 'email', 'orchestra_type1', 'orchestra_type2', 'prefecture', 'address', 'created_at',)
    search_fields = ('orchestra_name', 'orchestra_name_kana', 'orchestra_type1', 'orchestra_type2', 'email', 'prefecture', 'address',)
    ordering = ('created_at',)

admin.site.register(Orchestra, OrchestraAdmin)
