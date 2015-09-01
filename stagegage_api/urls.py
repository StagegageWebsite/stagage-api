from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from users import views as user_views
from stagegage.views import *

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'festivals', FestivalViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^sign_up/$', user_views.SignUp.as_view(), name='sign_up'),
    url(r'^login/$', user_views.Login.as_view(), name='login'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^notifications/', include('push_notifications.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
