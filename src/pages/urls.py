from django.urls import re_path

from . import views

app_name = 'pages'
urlpatterns = (
    re_path(r'^(?P<page_slug>.+)/$', views.page, name='page'),
)
