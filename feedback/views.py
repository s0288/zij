from django.shortcuts import redirect, render

from .forms import FeedbackItemForm


def index(request):
    return render(request, "feedback/index.html")


def add_feedback_item(request):
    form = FeedbackItemForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.username = request.user
        obj.save()
        return redirect("feedback:index")
    return render(request, "feedback/add_feedback_item_form.html", {"form": form})
