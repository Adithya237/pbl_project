from django.contrib import admin
from .models import PDFDocument

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'uploaded_at')
    search_fields = ('title',)
