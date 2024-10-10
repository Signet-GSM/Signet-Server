from rest_framework.viewsets import ModelViewSet

from gallery.models import Gallery
from gallery.serializers import GallerySerializer


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.filter(active=True)
    serializer_class = GallerySerializer
