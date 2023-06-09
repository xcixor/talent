from .base import *
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEBUG = True
ALLOWED_HOSTS = ['*']


# ckeditor configs
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
