from .models import PracticeInfo
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class PracticeInfoAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Practice info'), {'fields': ('title', 'content', 'orchestra')}),
    )
    list_display = ('title', 'content', 'orchestra',)
    search_fields = ('title', 'content', 'orchestra',)
    ordering = ('created_at',)
    
admin.site.register(PracticeInfo, PracticeInfoAdmin)
