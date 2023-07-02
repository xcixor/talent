from blog.models import Post


def posts(request):
    return {'posts': Post.objects.filter(status='publish')}
