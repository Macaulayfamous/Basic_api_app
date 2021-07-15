
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import MovieViewSet, ActionViewSet, ComedyViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register('', MovieViewSet)
router.register('action', ActionViewSet)
router.register('comedy', ComedyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
