from django.urls import path
from .views import handle_bot_request, poll_updates

urlpatterns = [
    path('update/<str:token>/', handle_bot_request),
    path('poll/<str:token>/', poll_updates)
]
