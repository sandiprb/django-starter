from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_label = 'core'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
