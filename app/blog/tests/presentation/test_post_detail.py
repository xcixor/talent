from django.test import TestCase
from django.urls import reverse
from django.views.generic import DetailView
from blog.presentation.views import PostDetailView


class PostDetailViewTestCase(TestCase):

    fixtures = [
        'blog/fixtures/posts/posts.json'
    ]

    def test_view_properties(self):
        self.assertTrue(issubclass(PostDetailView, DetailView))

    def test_get_post_page_succeeds(self):
        response = self.client.get(
            reverse('blog:post_detail', kwargs={'slug': 'slug-two'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_adds_blog_instance_to_context(self):
        response = self.client.get(
            reverse('blog:post_detail', kwargs={'slug': 'slug-two'}))
        self.assertTrue(response.context.get('post'))
