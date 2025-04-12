from django.shortcuts import render,redirect
from django.views.generic import ListView, View
from apps.bookings.models import Booking
from apps.bookings.task import process_bookings_task
from core.views import LoginRequiredMixinView

# Create your views here.

class BookingListView(LoginRequiredMixinView, ListView):
  model = Booking
  template_name = 'booking_list.html'
  context_object_name = "bookings"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    return context
  

class BookingProcessView(LoginRequiredMixinView, View):
  def get(self, request):
    return render(request, 'booking_process.html')
  
  def post(self, request):
    action = request.POST.get('action')

    if action == 'process':
      process_bookings_task()

    return redirect('booking_process')




