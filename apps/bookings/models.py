from django.db import models

from core.models import BaseModel
from apps.schedules.models import Hour, STATUS_CHOICES


class Booking(BaseModel):
  date = models.DateField()
  hour = models.ForeignKey(Hour, on_delete=models.CASCADE )
  name = models.CharField(max_length=255)
  status = models.CharField(max_length=255, choices=STATUS_CHOICES)

  class Meta:
    unique_together = ('date', 'hour')

  def day_date(self):
    return self.date.strftime('%A, %d %B %Y')
  




