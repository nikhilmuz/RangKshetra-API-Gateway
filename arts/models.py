# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Images(models.Model):
  art = models.FilePathField()
  caption = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)
  uploader = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='arts',on_delete=models.CASCADE)