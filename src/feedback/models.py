from django.db import models

from zij.models import CustomUser


class FeedbackItem(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback_item_choice = models.CharField(max_length=128)
    score = models.IntegerField(
        choices=[
            (5, "very positive"),
            (4, "positive"),
            (3, "neutral"),
            (2, "area to improve"),
            (1, "area to improve a lot"),
        ],
        blank=True,
        null=True,
    )
    description = models.CharField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}:{self.feedback_item_choice}"
