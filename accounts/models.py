from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    zotero_api_key = models.CharField(max_length=100, blank=True, null=True)
    zotero_user_id = models.CharField(max_length=100, blank=True, null=True)
    # add additional fields in here

    def __str__(self):
        return self.username