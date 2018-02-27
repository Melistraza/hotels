from django.utils import timezone
from rest_framework import serializers

from apps.rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            'pk', 'status', 'updated_at', 'created_at',
            'arrival_at', 'departure_at', 'number',
            'guest', 'notes', 'amount')
        read_only_fields = ('updated_at', 'created_at', 'status')

    def validate_arrival_at(self, value):
        if timezone.now().date() >= value:
            raise serializers.ValidationError("Date should be in future")
        return value

    def validate_departure_at(self, value):
        if timezone.now().date() >= value:
            raise serializers.ValidationError("Date should be in future")
        return value

    def validate(self, data):
        if data['departure_at'] < data['arrival_at']:
            raise serializers.ValidationError("The arrival date should be greater or equal to the date of departure")
        return data

    def update(self, instance, validated_data):
        delta = timezone.now() - instance.updated_at
        if delta.total_seconds() // 60:
            raise serializers.ValidationError('You can make changes only once a minute')
        return super(RoomSerializer, self).update(instance, validated_data)
