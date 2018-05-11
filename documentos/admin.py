from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


admin.site.register(DocumentTerm)
admin.site.register(Term)