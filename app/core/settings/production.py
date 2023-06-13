from .base import *
from google.oauth2 import service_account

# production settings
DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
ALLOWED_HOSTS = [
    'https://talent-staging-kr2eq6piia-ue.a.run.app',
    'https://*.infinitetalent.co.ke/']

CSRF_TRUSTED_ORIGINS = [
    'https://talent-staging-kr2eq6piia-ue.a.run.app',
    'https://*.infinitetalent.co.ke/']

# static files config
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# media files config
MEDIA_URL = os.environ.get('GS_BUCKET_URL')
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.environ.get('GS_BUCKET_NAME')
GS_LOCATION = os.environ.get('GS_LOCATION')
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.environ.get('GS_CREDENTIALS')
)

# ckeditor config
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "logs/prod.log",
            'maxBytes': 100000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'apps': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
