
from django.conf.urls import url, include

from django.contrib import admin

urlpatterns = [
    url(r'^cquiz/', include('cquiz.urls')),
    url(r'^admin/', admin.site.urls),
]
