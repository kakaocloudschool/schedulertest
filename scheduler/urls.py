from django.urls import path
from .views import (
    new_schedule,
    scheduler,
    schedule_list,
    jobadd,
)

urlpatterns = [
    path("schedule_list/<str:pk>", schedule_list, name="schedule_list"),
    path("new_schedule", new_schedule, name="new_schedule"),
    path("scheduler", scheduler, name="scheduler"),
    path("jobadd/<str:pk>", jobadd, name="jobadd"),
]