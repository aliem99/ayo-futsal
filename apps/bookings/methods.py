import time

from .models import Booking
from apps.schedules.models import Schedule

def process_booking():
  print(" Processing bookings ")
  schedulees = Schedule.objects.all()

  for schedulee in schedulees:
    status = schedulee.status
    print(f"Processing schedule for booking {schedulee.name} status {schedulee.status}")

    if status in ('pending', 'cancelled'):
      print(f"Skip booking for schedule {schedulee.date}")
      continue

    existing = Booking.objects.filter(date=schedulee.date,
    hour=schedulee.hour, name=schedulee.name).first()

    if existing:
      print(f"Booking already exist for {schedulee.name} on {schedulee.date}")
      continue

    booking = Booking.objects.create(date=schedulee.date, hour=schedulee.hour, name=schedulee.name, status=status)

    time.sleep(10)
 
    booking.status = 'confirmed'
    booking.save()

    time.sleep(10)
    print(f"Booking for schedule {schedulee.date} confirmed!")