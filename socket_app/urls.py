from django.urls import path
from .views import send_event

urlpatterns = [
  path('', send_event, name="create-socket"),
]
