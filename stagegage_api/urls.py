from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from stagegage.views import *

stagegage_urls = [
    url(r'^artists/$', ArtistList.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>[0-9]+)/$', ArtistDetail.as_view(), name='artist_detail'),
    url(r'^festivals/$', FestivalList.as_view(), name='festival_list'),
    url(r'^festivals/(?P<pk>[0-9]+)/$', FestivalDetail.as_view(), name='festival_detail'),
]

third_party_urls = [
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^notifications/', include('push_notifications.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = stagegage_urls + third_party_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
