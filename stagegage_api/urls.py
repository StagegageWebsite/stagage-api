from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from users import views as user_views
from stagegage.views import *

stagegage_urls = [
    url(r'^artists/$', ArtistList.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>[0-9]+)/$', ArtistDetail.as_view(), name='artist_detail'),
    url(r'^festivals/$', FestivalList.as_view(), name='festival_list'),
    url(r'^festivals/(?P<pk>[0-9]+)/$', FestivalDetail.as_view(), name='festival_detail'),
]

user_urls = [
    url(r'^sign_up/$', user_views.SignUp.as_view(), name='sign_up'),
    url(r'^login/$', user_views.Login.as_view(), name='login'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

misc_urls = [
    url(r'^notifications/', include('push_notifications.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = stagegage_urls + user_urls + misc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
