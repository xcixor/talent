"""Sets up a common testing environment."""
import os
import re
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from core.settings.base import BASE_DIR

User = get_user_model()


class BaseTestCase(TestCase):
    """Create the resources required for testing"""

    def delete_test_images(self, path):
        if os.path.isdir(str(BASE_DIR) + path):
            for entry in os.listdir(str(BASE_DIR) + path):
                if re.match('^test_image', entry):
                    os.remove(str(BASE_DIR) + path + entry)

    def get_image(self):
        image_path = str(BASE_DIR) + "/media/tests/test_image.png"
        mock_image = SimpleUploadedFile(
            name="test_image.png", content=open(image_path, 'rb').read(),
            content_type='image/png'
        )
        return mock_image

    def create_logged_in_admin(self):
        self.logged_in_admin = Client()
        superuser = User.objects.create_superuser(
            'super@user.com', 'admin2022')
        self.logged_in_admin.force_login(superuser)
