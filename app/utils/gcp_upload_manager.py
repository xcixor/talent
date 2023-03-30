import os
import datetime
from google.cloud import storage


class GoogleCloudStorageFileTransferManager(object):

    def __init__(self, blob_name, content_type, upload_location):
        self.cloud_storage_bucket = os.environ.get(
            'GS_BUCKET_NAME') + '/' + os.environ.get(
            'GS_LOCATION') + upload_location
        self.gs_credentials = os.environ.get('GS_CREDENTIALS')
        self.storage_client = storage.Client.from_service_account_json(
            self.gs_credentials)
        self.version = "v4"

        self.blob_name = blob_name
        self.content_type = content_type
        self.download_url = None

        self.object_name = None

    def generate_signed_upload_url(self):
        bucket = self.storage_client.bucket(self.cloud_storage_bucket)
        blob = bucket.blob(self.blob_name)
        url = blob.generate_signed_url(
            version=self.version,
            expiration=datetime.timedelta(minutes=60),
            method="PUT",
            content_type=self.content_type
        )
        self.download_url = self.generate_signed_download_url()
        self.object_name = blob.name
        return url

    def generate_signed_download_url(self):
        """Generates a v4 signed URL for downloading a blob.
        """
        bucket = self.storage_client.bucket(self.cloud_storage_bucket)
        blob = bucket.blob(self.blob_name)
        url = blob.generate_signed_url(
            version=self.version,
            expiration=datetime.timedelta(days=7),
            method="GET",
        )
        return url

    def set_blob_metadata(self, blob_name, metadata):
        bucket = self.storage_client.bucket(self.cloud_storage_bucket)
        blob = bucket.get_blob(blob_name)
        blob.metadata = metadata
        blob.patch()
        return blob.metadata

    def set_object_content_disposition(self, blob_name):
        bucket = self.storage_client.bucket(self.cloud_storage_bucket)
        blob = bucket.get_blob(blob_name)
        blob.content_disposition = "attachment"
        blob.patch()
        return True
