import cloudinary
import cloudinary.uploader
from django.core.files.storage import Storage
from django.conf import settings
import os

class CloudinaryStorage(Storage):
    
    def __init__(self):
        cloudinary.config(
            cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key    = settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret = settings.CLOUDINARY_STORAGE['API_SECRET'],
            secure     = True
        )

    def _save(self, name, content):
        # Upload to cloudinary
        response = cloudinary.uploader.upload(
            content,
            resource_type = 'raw',
            public_id     = name.replace('/', '_'),
            overwrite     = True
        )
        return response['secure_url']

    def url(self, name):
        # If already a full URL return as is
        if name.startswith('http'):
            return name
        return name

    def exists(self, name):
        return False

    def _open(self, name, mode='rb'):
        pass

    def delete(self, name):
        pass