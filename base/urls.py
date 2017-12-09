from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView  # TEMP

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index')  # TEMP
]
