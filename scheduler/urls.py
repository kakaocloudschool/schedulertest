from django.urls import path
from .views import (
    schedule_list,
    new_schedule,
    scheduler,
)

urlpatterns = [
    path("schedule_list/<str:pk>", schedule_list, name="schedule_list"),
    path("new_schedule/<str:pk>", new_schedule, name="new_schedule"),

    path("scheduler", scheduler, name="scheduler"),
]