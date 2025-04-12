from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path("",include('apps.authentications.urls')),
    path("",include('apps.bookings.urls')),
    path("",include('apps.schedules.urls')),

]
