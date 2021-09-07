from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from profile_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)