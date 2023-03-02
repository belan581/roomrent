from django.db import models
from django.contrib.auth.models import User

from rooms.models import Room

class Event(models.Model):
    STATUS_CHOICE = (
        (0, "Active"),
        (1, "Canceled")
    )
 
    TYPE_CHOICES = (
        (0, "Public"),
        (1, "Private"),
    )
    event_type = models.PositiveSmallIntegerField("Event type", choices=TYPE_CHOICES)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.PositiveSmallIntegerField("Status", choices=STATUS_CHOICE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
    
    def __str__(self) -> str:
        room = self.room.name
        date = str(self.date)
        start = str(self.start_time)
        end = str(self.end_time)
        status = self.status
        return f'Event on {room} at {date} since: {start} to {end}, status:{status}' 