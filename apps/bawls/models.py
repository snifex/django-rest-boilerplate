from django.db import models
from django.utils import timezone 
from django.utils.html import format_html
from core.storage_backends import PublicMediaStorage

from apps.media.models import Media
from apps.media.serializers import MediaSerializer

# Create your models here.

def rwi_thumbnail_directory(instance, filename):
    sanitized_name = instance.name.replace(" ","_")
    return "thumbnails/rwi/{0}/{1}".format(sanitized_name, filename)

def gallery_thumbnail_directory(instance, filename):
    sanitized_title = instance.title.replace(" ","_")
    return "thumbnails/gallery/{0}/{1}".format(sanitized_title, filename)

class GalleryItem(models.Model):
    type_options = (
        ("video", "Video"),
        ("image", "Image")
    )
    COLUMN_CHOICES = [(1, "1"), (2, "2")]
    ROW_CHOICES = [(1, "1"), (2, "2")]

    title = models.CharField(max_length=128)
    type = models.CharField(max_length=20, choices=type_options, default="image")
    logoUrl = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey(
        Media,
        on_delete=models.SET_NULL,
        related_name='gallery_thumbnail',
        blank=True,
        null=True
    )
    columns = models.PositiveIntegerField(choices=COLUMN_CHOICES, default=1)
    rows = models.PositiveIntegerField(choices=ROW_CHOICES, default=1)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["-title", "-created_at"]

    def __str__(self):
        return self.title

    def thumbnail_preview(self):
        if self.thumbnail:
            # Get the URL from the thumbnail's file field
            if hasattr(self.thumbnail, 'file') and self.thumbnail.file:
                if self.thumbnail.media_type == 'image':
                    return format_html(
                        '<img src="{}" style="max-height: 100px; max-width: 100px;" />', 
                        self.thumbnail.file.url
                    )
                else:
                    return format_html(
                        '<a href="{}" target="_blank">{}</a>',
                        self.thumbnail.file.url,
                        self.thumbnail.name or "View File"
                    )
        return "No thumbnail"
    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

class CoalitionMember(models.Model):
    # class CoalitionObjects(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset()

    name = models.CharField(max_length=128)
    logoUrl = models.TextField(blank=True, null=True)
    websiteUrl = models.TextField()
    thumbnail = models.ForeignKey(
        Media,
        on_delete=models.SET_NULL,
        related_name='coalition_thumbnail',
        blank=True,
        null=True
    )
    
    blockchain = models.CharField(max_length=200)
    narrative = models.TextField()

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager() #Default manager
    # coalitionObjects = CoalitionObjects() Custom

    class Meta:
        ordering = ["-name", "-created_at"]

    def __str__(self):
        return self.name
    
    def thumbnail_preview(self):
        if self.thumbnail:
            # Get the URL from the thumbnail's file field
            if hasattr(self.thumbnail, 'file') and self.thumbnail.file:
                if self.thumbnail.media_type == 'image':
                    return format_html(
                        '<img src="{}" style="max-height: 100px; max-width: 100px;" />', 
                        self.thumbnail.file.url
                    )
                else:
                    return format_html(
                        '<a href="{}" target="_blank">{}</a>',
                        self.thumbnail.file.url,
                        self.thumbnail.name or "View File"
                    )
        return "No thumbnail"
    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
