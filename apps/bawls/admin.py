from django.contrib import admin
from .models import CoalitionMember, GalleryItem

from apps.media.models import Media

class MediaInline(admin.TabularInline):
    model = Media
    fields = ('order', 'name', 'type', 'media_type')
    extra = 1

# Register your models here.
@admin.register(CoalitionMember)
class CoallitionMemberAdmin(admin.ModelAdmin):
    list_display = ("name" , "logoUrl" ,"websiteUrl" ,"blockchain" ,"narrative","created_at", "updated_at", "thumbnail_preview",)
    search_fields = ("name", "blockchain", "narrative",)
    list_filter = ("name",)
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at",)
    # inlines = [MediaInline]
    
    
@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title" ,"type" ,"logoUrl" ,"columns" ,"rows", "created_at", "updated_at", "thumbnail_preview",)
    list_editable = ("columns", "rows")
    search_fields = ("title", "type", "columns", "rows",)
    list_filter = ("title","type", "updated_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at",)
    fieldsets = (
        ("General Information", {
            "fields": ("title", "type", "logoUrl", "thumbnail", "columns", "rows",)
        }),
        ("Dates", {
            "fields": ("created_at", "updated_at",)
        })
    )
    
