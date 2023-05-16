import datetime
import time

from ckeditor.fields import RichTextField
from django.db import models
from django.test.utils import freeze_time

from blog.tests.common import BlogsBaseTestCase
from blog.models import Post


class PostsModelsTestCase(BlogsBaseTestCase):

    def setUp(self):
        super(PostsModelsTestCase, self).setUp()
        self.create_logged_in_admin()

    def delete_post_instance_image(self, post_title):
        instance = Post.objects.filter(title=post_title).first()
        self.delete_test_images(f'/media/blog/{instance.slug}/')

    def test_post_model_contains_title_field(self):
        self.assertTrue(hasattr(Post, "title"))

    def test_post_model_contains_author_field(self):
        self.assertTrue(hasattr(Post, "author"))

    def test_max_length_for_post_is_100(self):
        self.assertEqual(Post.title.field.max_length, 100)

    def test_author_field_not_required_on_post_creation(self):
        create_post_response = self.logged_in_admin.post(
            "/cO4yp84DxO8LqagQUUo/blog/post/add/", {
                "title": "Title",
                "created_on": datetime.date.today(),
                "status": "draft",
                "content": "Post Content",
                "image": self.get_image(),
                "slug": "draft",
                "epigraph": "Post Epigraph"})
        self.assertRedirects(create_post_response,
                             "/cO4yp84DxO8LqagQUUo/blog/post/", 302)
        self.delete_post_instance_image("Title")

    def test_post_contains_created_on_date_field(self):
        self.assertTrue(hasattr(Post, "created_on"))

    def test_created_on_field_is_a_date_field(self):
        self.assertTrue(
            isinstance(getattr(Post, "created_on").field, models.fields.DateField))

    def create_post_with_date_2020_Jan_15(self):
        self.logged_in_admin.post(
            "/cO4yp84DxO8LqagQUUo/blog/post/add/", {
                "title": "Title",
                "created_on": datetime.date(2020, 1, 15),
                "status": "draft",
                "content": "Post Content",
                "image": self.get_image(),
                "epigraph": "Post Epigraph"})

    # @freeze_time(1095379199.75) # time frozen to 2004-09-16
    # def test_post_creation_date_is_per_calender_date_not_user_entry(self):
    #     self.create_post_with_date_2020_Jan_15()
    #     self.assertEqual(
    #         str(Post.objects.get(title="Title").created_on), "2004-09-16")

    def test_post_contains_status_field(self):
        self.assertTrue(hasattr(Post, "status"))

    def test_status_field_is_a_choice_field(self):
        self.assertTrue(
            isinstance(getattr(Post, "status").field, models.fields.CharField))

    def test_max_length_for_post_status_is_20(self):
        self.assertEqual(Post.status.field.max_length, 20)

    def test_status_choices_on_Post(self):
        self.assertListEqual(
            Post.PUBLICATION_STATUSES, [
                ('draft', 'Draft'), ('publish', 'Publish'),
                ('archive', 'Archive')
            ])

    def test_choices_for_status_char_field(self):
        self.assertEqual(Post.status.field.choices, Post.PUBLICATION_STATUSES)

    def test_set_default_for_status_field_to_publish(self):
        self.assertEqual(Post.status.field.default, "publish")

    def test_content_field_exists_on_Post(self):
        self.assertTrue(hasattr(Post, "content"))

    def test_content_is_a_rich_text_field(self):
        self.assertTrue(
            isinstance(getattr(Post, "content").field, RichTextField))

    @freeze_time(1095379199.75)  # time frozen to 2004-09-16
    def create_post_with_date_2004_09_16(self):
        self.logged_in_admin.post(
            "/cO4yp84DxO8LqagQUUo/blog/post/add/", {
                "title": "Post Title 1",
                "created_on": datetime.date.today(),
                "status": "draft",
                "content": "Post Content",
                "image": self.get_image(),
                "slug": "slug-two",
                "epigraph": "Post Epigraph"})

    @freeze_time(1243090800)  # time frozen to 2009-05-23
    def create_post_with_date_2009_05_23(self):
        res = self.logged_in_admin.post(
            "/cO4yp84DxO8LqagQUUo/blog/post/add/", {
                "title": "Post Title 2",
                "created_on": datetime.date.today(),
                "status": "draft",
                "slug": "slug-one",
                "content": "Post Content",
                "image": self.get_image(),
                "epigraph": "Post Epigraph"})

    @freeze_time(1394809200)  # time frozen to 2014-03-14
    def create_post_with_date_2014_03_14(self):
        self.logged_in_admin.post(
            "/cO4yp84DxO8LqagQUUo/blog/post/add/", {
                "title": "Post Title 3",
                "created_on": datetime.date.today(),
                "status": "draft",
                "content": "Post Content",
                "slug": "slug-three",
                "image": self.get_image(),
                "epigraph": "Post Epigraph"})

    def test_post_ordered_based_on_creation_date(self):
        self.create_post_with_date_2004_09_16()
        self.create_post_with_date_2009_05_23()
        self.create_post_with_date_2014_03_14()
        get_all_Posts = Post.objects.all()
        self.assertEqual(get_all_Posts[0].title, "Post Title 3")
        self.assertEqual(get_all_Posts[1].title, "Post Title 2")
        self.assertEqual(get_all_Posts[2].title, "Post Title 1")
        self.delete_post_instance_image("Post Title 3")
        self.delete_post_instance_image("Post Title 2")
        self.delete_post_instance_image("Post Title 1")

    def create_sample_post(self):
        blog = Post.objects.get_or_create(
            title="Post Title Publish", author="Admin",
            created_on=datetime.date.today(),
            status="publish", content="Post Content",
            epigraph="Post Epigraph", image=self.get_image())[0]
        return blog

    def test_post_contains_epigraph_field(self):
        self.assertTrue(hasattr(Post, "epigraph"))

    def test_post_has_image_attribute(self):
        self.assertTrue(hasattr(Post, "image"))

    def test_image_attribute_can_be_null_on_database(self):
        self.assertEqual(Post.image.field.null, False)

    def test_image_attribute_can_be_blank(self):
        self.assertEqual(Post.image.field.blank, False)
