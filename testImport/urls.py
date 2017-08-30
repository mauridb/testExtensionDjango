from django.conf.urls import url, include
from django.contrib import admin

from wizard import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='home'),

    # data wizard url
    url(r'^', include('data_wizard.urls')),
]


