from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_type', 'date', 'start_time', 'end_time', 'status', 'room']