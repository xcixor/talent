"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from infinite_admin.admin import custom_admin_site


urlpatterns = [
    path('cO4yp84DxO8LqagQUUo/advanced/', custom_admin_site.urls),
    path('cO4yp84DxO8LqagQUUo/', admin.site.urls),
    path('', include('index.presentation.urls', namespace='index')),
    path('accounts/', include('accounts.presentation.urls', namespace='accounts')),
    path('backup/', include('backup.presentation.urls', namespace='backup')),
    path('job/', include('job.presentation.urls', namespace='job')),
    path('shortlist/', include('shortlist.presentation.urls', namespace='shortlist')),
    path('about/', include('about.presentation.urls', namespace='about')),
    path('contact/', include('contact.presentation.urls', namespace='contact')),
    path('testimonials/', include('testimonials.presentation.urls',
         namespace='testimonials')),
    path('blog/', include('blog.presentation.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('chat/', include('chat.presentation.urls', namespace='chat')),
    path('careers/', include('careers.presentation.urls', namespace='careers')),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
else:
    urlpatterns.append(re_path(r'^media/(?P<path>.*)$', serve,
                               {'document_root': settings.MEDIA_ROOT}))
    urlpatterns.append(
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}))
