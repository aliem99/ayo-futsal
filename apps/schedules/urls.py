from django.urls import path
from .views import SceduleListView, add_schedule, edit_schedule, delete_schedule

urlpatterns = [
    path('schedules/', SceduleListView.as_view(), name='schedule_list' ),
    path('add_schedule/', add_schedule, name='add_schedule'),
    path('<str:pk>/edit/', edit_schedule, name='edit_schedule'),
     path('<str:pk>/delete/', delete_schedule, name='delete_schedule')
]
