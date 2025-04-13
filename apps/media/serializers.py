import datetime

from rest_framework import serializers
from django.conf import settings
from django.utils import timezone
from botocore.signers import CloudFrontSigner

from utils.s3_utils import rsa_signer
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = "__all__"

    def get_url(self, obj):
        if not obj.key:
            return None
        
        # cloudfront_key_id = settings.AWS_CLOUDFRONT_KEY_ID
        # signer = CloudFrontSigner(cloudfront_key_id, rsa_signer)
        # expire_date = timezone.now() + datetime.timedelta(seconds=60)
        object_url = f"https://{settings.AWS_S3_DOMAIN}/{obj.key}"
        # signed_url = signer.generate_presigned_url(object_url, date_less_than=expire_date)

        # return signed_url
        return object_url
