from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data =serializer.data
        event_type = data.get("event_type", 0)
        # You can't place an event, just an admin user
        if event_type == 1:
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED, headers=headers)
        date = data.get("date")
        # Room is reserved for an active event, select another day
        if Event.objects.filter(event_date = date, status=0):
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED, headers=headers)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)