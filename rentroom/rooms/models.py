from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "Room for event"
        verbose_name_plural = "Rooms for events"
    
    def __str__(self) -> str:
        return self.name