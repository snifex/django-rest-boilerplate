from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework_api.views import StandardAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, APIException

from .models import CoalitionMember, GalleryItem
from .serializers import CoallitionSerializer, GallerySerializer
from core.permissions import HasValidAPIKey


class CoallitionListView(StandardAPIView):
    def get(self, request, *args, **kwargs):
        try:
            recent_only = request.query_params.get('recent', '').lower() == 'true'
            queryset = CoalitionMember.objects.all().order_by('-created_at')
            
            if recent_only:
                queryset = queryset[:5]
                
            if not queryset.exists():
                raise NotFound(detail="No posts found.")

            serialize_members = CoallitionSerializer(queryset, many=True).data

        except Exception as e:
            raise APIException(detail=f"An unexpected error occurred: {str(e)}")
        
        return self.response(serialize_members)
    
class GalleryItemsListView(StandardAPIView):
    def get(self, request, *args, **kwargs):
        try:
            recent_only = request.query_params.get('recent', '').lower() == 'true'
            queryset = GalleryItem.objects.all().order_by('-created_at')

            if recent_only:
                queryset = queryset[:5]
                
            if not queryset.exists():
                raise NotFound(detail="No posts found.")

            serialize_members = GallerySerializer(queryset, many=True).data
        
        except Exception as e:
            raise APIException(detail=f"An unexpected error ocureed: {str(e)}")
       
        return self.response(serialize_members)

# class CoallitionDetailView(APIView):
#     def get(self, request, name):
#         queryset = CoalitionMember.objects.get(name=name)
#         serialized_post = CoallitionSerializer(queryset).data
#         return Response(serialized_post)