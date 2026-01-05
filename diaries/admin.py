from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_public') # Kolom yang tampil di daftar
    list_filter = ('is_public', 'created_at')           # Filter di sebelah kanan
    search_fields = ('title', 'content')