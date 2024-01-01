from django import forms

from .models import FeedbackItem


class FeedbackItemForm(forms.ModelForm):
    feedback_item_choice_types = [
        ("communicates_well", "Communicates well"),
        ("attentive", "Attentive"),
        ("results_oriented", "Results oriented"),
        ("non_linear_thinking", "Non-linear thinking"),
        ("generates_ideas", "Generates ideas"),
        ("strategic_thinking", "Strategic thinking"),
        ("adapts_to_change", "Adapts to change"),
        ("assertive", "Assertive"),
        ("other", "Other"),
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
