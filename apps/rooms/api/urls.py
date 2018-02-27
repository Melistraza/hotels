from rest_framework import routers

from apps.rooms.api.views import RoomViewSet


router = routers.SimpleRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = router.urls
