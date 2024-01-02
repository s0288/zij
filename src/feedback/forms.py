from django import forms

from .models import FeedbackItem


class FeedbackItemForm(forms.ModelForm):
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
        fields = ("id", "feedback_item_choice", "score", "description")
        widgets = {
            "description": forms.Textarea(attrs={"cols": 25, "rows": 3}),
        }