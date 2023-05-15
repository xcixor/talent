import datetime
import os
import re

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from core.settings.base import BASE_DIR
from django.contrib.auth.models import User
from blog.models import Post
from common.tests import BaseTestCase


class BlogsBaseTestCase(BaseTestCase):

    def setUp(self):
        super(BlogsBaseTestCase, self).setUp()

    def create_sample_blog_post(self):
        blog = Post.objects.get_or_create(
            title="Blog Title Publish", author='Datamax Press',
            created_on=datetime.date.today(), status="Publish",
            content="Blog Content", epigraph="Blog Epigraph",
            caption_image=self.get_photo(),
            slug='blog-title-publish')[0]
        return blog

    def create_draft_blog(self):
        blog = Post.objects.get_or_create(
            title="Blog Title Publish", author='Datamax Press',
            created_on=datetime.date.today(), status="Draft",
            content="Draft Content", epigraph="Draft Epigraph",
            caption_image=self.get_photo())[0]
        return blog
