from django.test import TestCase
from django.urls import reverse_lazy
from django.views.generic import ListView
from blog.presentation.views import PostsHomeView


class PostsHomeViewTestCase(TestCase):

    fixtures = [
        'blog/fixtures/posts.json'
    ]

    def test_view_properties(self):
        self.assertTrue(issubclass(PostsHomeView, ListView))

    def test_get_posts_page_succeeds(self):
        response = self.client.get(reverse_lazy('blog:posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_base.html')

    def test_adds_posts_to_context(self):
        response = self.client.get(reverse_lazy('blog:posts'))
        self.assertTrue(response.context.get('posts'))
