from django.contrib import admin

from .models import FeedbackItem


@admin.register(FeedbackItem)
class FeedbackItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "feedback_item_choice",
        "score",
        "description",
        "created_at",
        "updated_at",
    )  # Add 'created_at' to the list_display

    # Your other admin options here
