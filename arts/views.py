# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import boto3
import time, datetime
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from rangkshetra.settings import *
from .models import *
from django.views.decorators.csrf import *
from .paginations import *


class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        upload_serializer = UploadSerializer(data=request.data)
        if upload_serializer.is_valid():
            s3 = boto3.client(
                's3',
                aws_access_key_id=AWS_KEY,
                aws_secret_access_key=AWS_SECRET,
            )
            filename = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')) + str(
                os.path.splitext(upload_serializer.validated_data['art'].name)[1])
            s3.upload_fileobj(upload_serializer.validated_data['art'], S3_BUCKET_NAME,
                              'arts/' + str(request.user.id) + '/' + filename)
            upload_serializer.save(art=str(request.user.id) + "/" + filename, uploader=request.user)
            return Response(upload_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
    def post(self, request, *args, **kwargs):
        imageObject = Images.objects.get(id=request.POST['id'])
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET,
        )
        if imageObject.uploader == request.user:
            s3.delete_object(Bucket=S3_BUCKET_NAME, Key='arts/'+imageObject.art)
            imageObject.delete()
            return Response({'status': 'Successfully Deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)


class SelfUploadsView(generics.ListAPIView):
    serializer_class = FeedSerializer
    pagination_class = UploadsPagination

    def get_queryset(self):
        return Images.objects.filter(uploader=self.request.user)


class FeedsView(generics.ListAPIView):
    permission_classes = ()
    queryset = Images.objects.all()
    serializer_class = FeedSerializer
    pagination_class = FeedPagination
