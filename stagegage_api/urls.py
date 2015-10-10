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
    # (r'^notifications/', include('push_notifications.urls')),
    # (r'^docs/', include('rest_framework_swagger.urls')),
    (r'^admin/', include(admin.site.urls)),
    # (r'^accounts/', include('allauth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
