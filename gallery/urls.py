from django.urls import path

from gallery.viewsets import GalleryViewSet

gallery_list = GalleryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', gallery_list)
]