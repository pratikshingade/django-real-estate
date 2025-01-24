from django.urls import path

from . import views

urlpatterns = [
    path("", views.send_enquiry_email_api_view, name="send-enquiry-mail"),
]
