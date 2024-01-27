from django import forms

from zij.models import CustomUser

from .models import FeedbackItem


class FeedbackItemForm(forms.ModelForm):
    feedback_recipient = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(), empty_label="Select a user"
    )
    feedback_item_choice_types = [
        ("Communicates well", "Communicates well"),
        ("Attentive", "Attentive"),
        ("Results oriented", "Results oriented"),
        ("Non-linear thinking", "Non-linear thinking"),
        ("Generates ideas", "Generates ideas"),
        ("Strategic thinking", "Strategic thinking"),
        ("Adapts to change", "Adapts to change"),
        ("Assertive", "Assertive"),
        ("Other", "Other"),
    ]
    feedback_item_choice = forms.CharField(
        widget=forms.Select(choices=feedback_item_choice_types)
    )

    class Meta:
        model = FeedbackItem
        fields = (
            "id",
            "feedback_recipient",
            "feedback_item_choice",
            "score",
            "description",
        )
        widgets = {
            "description": forms.Textarea(attrs={"cols": 25, "rows": 3}),
        }
