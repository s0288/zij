from django import forms

from zij.models import CustomUser

from .models import FeedbackItem


class FeedbackItemForm(forms.ModelForm):
    feedback_recipient = forms.ModelChoiceField(
        queryset=CustomUser.objects.exclude(is_superuser=True),
        empty_label="Select a user",
    )
    feedback_item_choice_types = [
        ("Adapts to change", "Adapts to change"),
        ("Analytical competence", "Analytical competence"),
        ("Assertive", "Assertive"),
        ("Attentive", "Attentive"),
        ("Communicates well", "Communicates well"),
        ("Generates ideas", "Generates ideas"),
        ("Non-linear thinking", "Non-linear thinking"),
        ("Results oriented", "Results oriented"),
        ("Software design patterns", "Software design patterns"),
        ("Strategic thinking", "Strategic thinking"),
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
