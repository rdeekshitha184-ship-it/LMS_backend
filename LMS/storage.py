# # # import cloudinary
# # # import cloudinary.uploader
# # # from django.core.files.storage import Storage
# # # from django.conf import settings
# # # import os

# # # class CloudinaryStorage(Storage):
    
# # #     def __init__(self):
# # #         cloudinary.config(
# # #             cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
# # #             api_key    = settings.CLOUDINARY_STORAGE['API_KEY'],
# # #             api_secret = settings.CLOUDINARY_STORAGE['API_SECRET'],
# # #             secure     = True
# # #         )

# # #     def _save(self, name, content):
# # #         # Upload to cloudinary
# # #         response = cloudinary.uploader.upload(
# # #             content,
# # #             resource_type = 'raw',
# # #             public_id     = name.replace('/', '_'),
# # #             overwrite     = True
# # #         )
# # #         return response['secure_url']

# # #     def url(self, name):
# # #         # If already a full URL return as is
# # #         if name.startswith('http'):
# # #             return name
# # #         return name

# # #     def exists(self, name):
# # #         return False

# # #     def _open(self, name, mode='rb'):
# # #         pass

# # #     def delete(self, name):
# # #         pass


# # import cloudinary
# # import cloudinary.uploader
# # from django.core.files.storage import Storage
# # from decouple import config

# # # Configure cloudinary directly
# # cloudinary.config(
# #     cloud_name = config('CLOUDINARY_CLOUD_NAME'),
# #     api_key    = config('CLOUDINARY_API_KEY'),
# #     api_secret = config('CLOUDINARY_API_SECRET'),
# #     secure     = True
# # )

# # class CloudinaryStorage(Storage):

# #     def _save(self, name, content):
# #         # Clean filename
# #         clean_name = name.replace('/', '_').replace(' ', '_')
        
# #         # Upload to cloudinary as raw file
# #         response = cloudinary.uploader.upload(
# #             content,
# #             resource_type = 'raw',
# #             public_id     = clean_name,
# #             overwrite     = True,
# #             access_mode   = 'public',    # ← ADD THIS
# #             type          = 'upload'     # ← ADD THIS
# #         )
# #         # Return the secure URL directly
# #         return response['secure_url']

# #     def url(self, name):
# #         # If already a full URL return as is
# #         if name and name.startswith('http'):
# #             return name
# #         return name

# #     def exists(self, name):
# #         return False

# #     def _open(self, name, mode='rb'):
# #         pass

# #     def delete(self, name):
# #         pass

# #     def size(self, name):
# #         return 0


# import cloudinary
# import cloudinary.uploader
# from django.core.files.storage import Storage
# from decouple import config

# cloudinary.config(
#     cloud_name = config('CLOUDINARY_CLOUD_NAME'),
#     api_key    = config('CLOUDINARY_API_KEY'),
#     api_secret = config('CLOUDINARY_API_SECRET'),
#     secure     = True
# )

# class CloudinaryStorage(Storage):

#     def _save(self, name, content):
#         clean_name = name.replace('/', '_').replace(' ', '_')
        
#         response = cloudinary.uploader.upload(
#             content,
#             resource_type = 'raw',
#             public_id     = clean_name,
#             overwrite     = True,
#             access_mode   = 'public',
#             type          = 'upload',
#             format        = 'pdf'
#         )
#         # Return URL with fl_attachment for direct download
#         url = response['secure_url']
#         return url

#     def url(self, name):
#         if name and name.startswith('http'):
#             return name
#         return name

#     def exists(self, name):
#         return False

#     def _open(self, name, mode='rb'):
#         pass

#     def delete(self, name):
#         pass

#     def size(self, name):
#         return 0

import cloudinary
import cloudinary.uploader
from django.core.files.storage import Storage
from decouple import config

cloudinary.config(
    cloud_name = config('CLOUDINARY_CLOUD_NAME'),
    api_key    = config('CLOUDINARY_API_KEY'),
    api_secret = config('CLOUDINARY_API_SECRET'),
    secure     = True
)

class CloudinaryStorage(Storage):

    def _save(self, name, content):
        clean_name = name.replace('/', '_').replace(' ', '_')
        
        response = cloudinary.uploader.upload(
            content,
            resource_type = 'auto',  # ← auto detects PDF
            public_id     = clean_name,
            overwrite     = True,
        )
        
        # Build direct URL for PDF
        url = response['secure_url']
        return url

    def url(self, name):
        if name and name.startswith('http'):
            return name
        return name

    def exists(self, name):
        return False

    def _open(self, name, mode='rb'):
        pass

    def delete(self, name):
        pass

    def size(self, name):
        return 0