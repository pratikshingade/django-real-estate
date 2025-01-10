from django.urls import path

from . import views

urlpatterns = [
    path('<str:profile_id>/', views.create_agent_review_api_view, name='create-rating'),
]
