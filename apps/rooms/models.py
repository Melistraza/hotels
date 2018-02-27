from django.utils import timezone

from django.db import models


class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    arrival_at = models.DateField()
    departure_at = models.DateField(blank=True, null=True)
    number = models.IntegerField(unique=True)

    guest = models.CharField(max_length=256, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    @property
    def status(self):
        now = timezone.now().date()
        if self.arrival_at <= now and not self.departure_at or (
                self.departure_at and self.departure_at > now and self.arrival_at <= now):
            return 'in-house'
        elif now <= self.arrival_at:
            return 'future reservation'
        elif self.departure_at and now >= self.departure_at:
            return 'checked out'
        return 'unavailable'
