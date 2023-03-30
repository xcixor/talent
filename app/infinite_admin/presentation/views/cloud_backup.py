from pathlib import Path
from django.conf import settings
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
import requests
from utils import GoogleCloudStorageFileTransferManager


def upload_file_to_gcp(file_name, file_path, location, content_type='text/plain'):
    manager = GoogleCloudStorageFileTransferManager(
        file_name, content_type, location)
    url = manager.generate_signed_upload_url()
    headers = {'content-type': content_type}
    files = {file_name: open(file_path, 'rb')}
    response = requests.put(url, headers=headers, files=files)
    print()
    return {'status': response.status_code, 'message': response.text}


def backup_logs():
    response = {
        'status': 0,
        'message': ''
    }
    try:
        log_file = str(settings.BASE_DIR)[:-4] + 'logs/prod.log'
        with open(log_file, 'r') as file:
            if not settings.DEBUG:
                extension = Path(file.name).suffix
                filename = Path(file.name).stem + extension
                upload_location = '/LOGS'
                status = upload_file_to_gcp(
                    filename, file.name, upload_location, content_type='text/x-log')
                response['status'] = status['status']
                response['message'] = status['message']
    except Exception as err:
        response['status'] = 404
        response['message'] = str(err)
    finally:
        return response


class CloudBackupView(View):

    def get(self, request, *args, **kwargs):
        response = backup_logs()
        message = response['message']
        status = response['status']
        if status == 200:
            success_message = _(f'Upload Successful. {message}')
            messages.add_message(
                self.request, messages.SUCCESS, success_message)
        else:
            error_message = _(
                f'status: {status}, Something went wrong. {message}')
            messages.add_message(
                self.request, messages.ERROR, error_message)
        return redirect(reverse('admin_advanced:logging'))
