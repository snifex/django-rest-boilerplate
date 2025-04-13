from django.contrib import admin
from django.utils.html import format_html
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'preview', 'created_at')
    list_filter = ('media_type', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('preview', 'size', 'type', 'key', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('file', 'name', 'media_type', 'order')
        }),
        ('Advanced', {
            'fields': ('size', 'type', 'key'),
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def preview(self, obj):
        if obj.file:
            if obj.media_type == 'image':
                return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.file.url)
            elif obj.media_type in ['video', 'audio']:
                return format_html(
                    '<p>{}</p><a href="{}" target="_blank">View {}</a>',
                    obj.file.name,
                    obj.file.url,
                    obj.media_type.capitalize()
                )
            else:
                return format_html(
                    '<p>{}</p><a href="{}" target="_blank">Download</a>',
                    obj.file.name,
                    obj.file.url
                )
        return "No file"
    preview.short_description = 'Preview'