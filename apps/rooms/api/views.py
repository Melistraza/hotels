from rest_framework import viewsets

from apps.rooms.api.serializers import RoomSerializer
from apps.rooms.models import Room


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
