from django.db import models
from core.models import BaseModel

# Create your models here.

STATUS_CHOICES =(
    ('confirmed', 'Confirmed'),
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
  )

class Hour(models.Model):
  hour_list = models.CharField(max_length=255)

  class Meta:
    ordering = ('hour_list',)

  def __str__(self):
    return self.hour_list

class Schedule(BaseModel):
  date = models.DateField()
  hour = models.ForeignKey(Hour, on_delete=models.CASCADE )
  name = models.CharField(max_length=255)
  status = models.CharField(max_length=255, choices=STATUS_CHOICES)

  class Meta:
    unique_together = ('date', 'hour')

  def day_date(self):
    return self.date.strftime('%A, %d %B %Y')
  



