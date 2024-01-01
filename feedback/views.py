from django.shortcuts import redirect, render

from .forms import FeedbackItemForm
from .models import FeedbackItem


def index(request):
    feedback_item_list = FeedbackItem.objects.order_by("id")
    return render(
        request, "feedback/index.html", {"feedback_items": feedback_item_list}
    )


def add_feedback_item(request):
    form = FeedbackItemForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.username = request.user
        obj.save()
        return redirect("feedback:index")
    return render(request, "feedback/add_feedback_item_form.html", {"form": form})
