from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('announcements', views.AnnouncementModelViewSet, basename='announcements')
urlpatterns = [] + router.urls