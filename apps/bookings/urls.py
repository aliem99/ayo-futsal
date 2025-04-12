from django.urls import path
from .views import BookingListView, BookingProcessView

urlpatterns = [
    path('dashboard/', BookingListView.as_view(), name='booking_list'),
    path('process/', BookingProcessView.as_view(), name='booking_process')
]
