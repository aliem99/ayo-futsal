from huey.contrib.djhuey import task
from .methods import process_booking

@task()
def process_bookings_task():
  process_booking()