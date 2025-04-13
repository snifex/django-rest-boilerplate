from rest_framework import serializers
from .models import CoalitionMember, GalleryItem
from apps.media.serializers import MediaSerializer

class CoallitionSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer()

    class Meta:
        model = CoalitionMember
        fields = [
            "name",
            "logoUrl",
            "websiteUrl",
            "thumbnail",
            "blockchain",
            "narrative",
        ]

class GallerySerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer()

    class Meta:
        model = GalleryItem
        fields = [
            "title",
            "type",
            "logoUrl",
            "thumbnail",
            "columns",
            "rows",
        ]