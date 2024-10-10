from rest_framework import serializers

from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        extra_kwargs = {
            'view': {'read_only': True},
            'active': {'read_only': True},
            'created': {'read_only': True},
            'modified': {'read_only': True},
        }