from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path("feedback/", views.index, name="index"),
    path("add_feedback_item/", views.add_feedback_item, name="add_feedback_item"),
    path(
        "edit_feedback_item/<str:feedback_item_id>",
        views.edit_feedback_item,
        name="edit_feedback_item",
    ),
    path(
        "delete_feedback_item/<str:feedback_item_id>",
        views.delete_feedback_item,
        name="delete_feedback_item",
    ),
]
