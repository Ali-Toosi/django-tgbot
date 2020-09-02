from django.urls import path
from .views import handle_bot_request

urlpatterns = [
    path('update/', handle_bot_request)
]
