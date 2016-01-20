"""Register urls for incoming API requests.

The router class has predetermined urls patterns for viewsets so we don't need
to define every route for our API.
See http://www.django-rest-framework.org/api-guide/routers/ for more detail.
"""

from django.conf import settings
from django.conf.urls import include, patterns
from django.conf.urls.static import static
from django.contrib import admin
from stagegage.views import ArtistViewSet, FestivalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, base_name='artists')
router.register(r'festivals', FestivalViewSet, base_name='festivals')

urlpatterns = patterns('',
    (r'^', include(router.urls)),
    (r'^auth/', include('rest_framework_social_oauth2.urls')),
    (r'^docs/', include('rest_framework_swagger.urls')),
    (r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
