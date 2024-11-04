from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlight',)
# Register your models here.
admin.site.register(Snippet,SnippetAdmin)