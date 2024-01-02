from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path("feedback/", views.index, name="index"),
    path("add_feedback_item/", views.add_feedback_item, name="add_feedback_item"),
]
