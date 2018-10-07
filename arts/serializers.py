from rest_framework import serializers
from .models import *
from rangkshetra.settings import *
class UploadSerializer(serializers.ModelSerializer):
        art = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
        class Meta():
            model = Images
            fields = ('art', 'caption', 'timestamp')

        def to_representation(self, instance):
            ret = super(UploadSerializer, self).to_representation(instance)
            ret.pop('art', None)
            ret['status'] = 'Uploaded Successfully'
            return ret


class FeedSerializer(serializers.ModelSerializer):
    art = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    class Meta():
        model = Images
        fields = ('id', 'art', 'caption', 'timestamp', 'likes', 'uploader')

    def create(self, validated_data):
        validated_data['art'] = ARTS_URL_ROOT+validated_data['art']
        return Images(**validated_data)

    def to_representation(self, instance):
        ret = super(FeedSerializer,self).to_representation(instance)
        ret['art'] = ARTS_URL_ROOT+ret['art']
        return ret