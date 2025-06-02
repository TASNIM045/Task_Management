from django.urls import path
from tasks.views import show_task,print_name

urlpatterns = [
    path('show-task/', show_task)
    path('print-name/', print_name)
]