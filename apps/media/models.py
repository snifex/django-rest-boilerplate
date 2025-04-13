from django.utils import timezone
from django.db import models
import uuid
from django.core.validators import FileExtensionValidator

# TODO: Arreglar las carpetas en donde se guarda media

class Media(models.Model):
    MEDIA_TYPES = (
        ("image", "Image"),
        ("video", "Video"),
        ("document", "Document"),
        ("audio", "Audio")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=256, blank=True)
    file = models.FileField(
        null=True,  
        blank=True, 
        upload_to='media/',
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'jpg', 'jpeg', 'png', 'gif',  # Images
                'mp4', 'mov', 'avi',           # Videos
                'mp3', 'wav',                  # Audio
                'pdf', 'doc', 'docx', 'txt'    # Documents
            ])
        ]
    )
    size = models.CharField(max_length=256, blank=True, editable=False)
    type = models.CharField(max_length=256, blank=True, editable=False)
    key = models.CharField(max_length=256, blank=True, editable=False)
    media_type = models.CharField(max_length=30, choices=MEDIA_TYPES)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        # Auto-populate name if not provided
        if not self.name and self.file:
            self.name = self.file.name
        
        # Auto-detect media type based on file extension
        if self.file:
            extension = self.file.name.split('.')[-1].lower()
            if extension in ['jpg', 'jpeg', 'png', 'gif']:
                self.media_type = 'image'
            elif extension in ['mp4', 'mov', 'avi']:
                self.media_type = 'video'
            elif extension in ['mp3', 'wav']:
                self.media_type = 'audio'
            else:
                self.media_type = 'document'
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or self.file.name if self.file else "Unnamed Media"