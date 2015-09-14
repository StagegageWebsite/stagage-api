from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from stagegage.views import ArtistViewSet, FestivalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'festivals', FestivalViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^notifications/', include('push_notifications.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
