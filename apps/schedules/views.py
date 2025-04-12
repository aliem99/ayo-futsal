from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from .models import Schedule, Hour
from core.views import LoginRequiredMixinView

# Create your views here.

class SceduleListView(LoginRequiredMixinView, ListView):
  model = Schedule
  template_name = "schedule_list.html"
  context_object_name = "schedules"

  def get_context_data(self, **kwargs):
    return super().get_context_data(**kwargs)


def add_schedule(request):
  error = None

  if request.method == 'POST':
    date = request.POST.get('date')
    hour_id = request.POST.get('hour')
    name = request.POST.get('name')
    payment_status = request.POST.get('payment_status')

    hour = Hour.objects.get(id=hour_id)

  
    if Schedule.objects.filter(date=date, hour=hour).exists():
      error = "Jam di tanggal tersebut sudah ada"

    else:
      schedule = Schedule(
        date=date,
        hour=hour,
        name=name,
        )

      if payment_status == 'lunas':
         schedule.status = 'confirmed'
      elif payment_status == 'dp':
        schedule.status = 'pending'
      elif payment_status == 'cancel':
        schedule.status = 'cancelled'

      schedule.save()
      return redirect('schedule_list')

  hours = Hour.objects.all()
  return render(request, 'add_schedule.html',{
    'title':'Tambah jadwal',
    'hours':hours,
    'error': error
  })
  
def edit_schedule(request,pk):
  schedule = get_object_or_404(Schedule, pk=pk)
  error = None

  if request.method == 'POST':
    date = request.POST.get('date')
    hour_id = request.POST.get('hour')
    name = request.POST.get('name')
    payment_status = request.POST.get('payment_status')

    hour = Hour.objects.get(id=hour_id)

  
    if Schedule.objects.exclude(pk=schedule.pk).filter(date=date, hour=hour).exists():
      error = "Jam di tanggal tersebut sudah ada"

    else:
        schedule.date = date
        schedule.hour = hour
        schedule.name = name
      

        if payment_status == 'lunas':
          schedule.status = 'confirmed'
        elif payment_status == 'dp':
          schedule.status = 'pending'
        elif payment_status == 'cancel':
          schedule.status = 'cancelled'

        schedule.save()
        return redirect('schedule_list')

  hours = Hour.objects.all()
  return render(request, 'add_schedule.html',{
    'title':'Edit Jadwal',
    'hours':hours,
    'error': error,
    'schedule': schedule,
  })

def delete_schedule(request, pk):
  schedule = get_object_or_404(Schedule,pk=pk)
  schedule.delete()

  return redirect('schedule_list')