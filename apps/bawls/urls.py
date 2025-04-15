from django.urls import path
from .views import CoallitionListView, GalleryItemsListView


urlpatterns = [
    path('coallitions/', CoallitionListView.as_view(), name="rwi_list"),
    path('gallery/', GalleryItemsListView.as_view(), name="gallery_items_list"),
    # path('coallitions/<name>', CoallitionDetailView.as_view(), name="rwi_detail"),
]