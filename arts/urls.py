from django.conf.urls import url
from .views import *
urlpatterns = [
  url(r'^upload/$', UploadView.as_view(), name='Arts Upload'),
  url(r'^like/$', LikeView.as_view(), name='Like Arts'),
  url(r'^delete/$', DeleteView.as_view(), name='Delete Art'),
  url(r'^myuploads/$', SelfUploadsView.as_view(), name='Uploaded Arts'),
  url(r'^feeds/$', FeedsView.as_view(), name='Arts Feed'),
]