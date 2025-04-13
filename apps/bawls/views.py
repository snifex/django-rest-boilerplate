from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework_api.views import StandardAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, APIException

from .models import CoalitionMember, GalleryItem
from .serializers import CoallitionSerializer, GallerySerializer
from core.permissions import HasValidAPIKey


class CoallitionListView(StandardAPIView):
    # permission_classes = [HasValidAPIKey]
    def get(self, request, *args, **kwargs):
        try:
            coallition_members = CoalitionMember.objects.all()

            if not coallition_members.exists():
                raise NotFound(detail="No posts found.")

            serialize_members = CoallitionSerializer(coallition_members, many=True).data

        except CoalitionMember.DoesNotExist:
            raise NotFound(detail="No posts found.")
        
        except Exception as e:
            raise APIException(detail=f"An unexpected error ocureed: {str(e)}")
        
        return self.response(serialize_members)
    
class GalleryItemsListView(StandardAPIView):
    def get(self, request, *args, **kwargs):
        try:
            gallery_items = GalleryItem.objects.all()

            if not gallery_items.exists():
                raise NotFound(detail="No gallery items found.")
            
            serialize_members = GallerySerializer(gallery_items, many=True).data
        
        except CoalitionMember.DoesNotExist:
                raise NotFound(detail="No gallery items found.")
        
        except Exception as e:
            raise APIException(detail=f"An unexpected error ocureed: {str(e)}")
       
        return self.response(serialize_members)


# class CoallitionDetailView(APIView):
#     def get(self, request, name):
#         queryset = CoalitionMember.objects.get(name=name)
#         serialized_post = CoallitionSerializer(queryset).data
#         return Response(serialized_post)