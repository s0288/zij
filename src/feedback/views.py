import datetime

import pytz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import FeedbackItemForm
from .models import FeedbackItem


def index(request):
    feedback_item_list = FeedbackItem.objects.order_by("id")
    return render(
        request, "feedback/index.html", {"feedback_items": feedback_item_list}
    )


@login_required
def add_feedback_item(request):
    form = FeedbackItemForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.username = request.user
        obj.save()
        return redirect("feedback:index")
    return render(request, "feedback/add_feedback_item_form.html", {"form": form})


@login_required
def edit_feedback_item(request, feedback_item_id):
    feedback_item = FeedbackItem.objects.get(pk=feedback_item_id)
    form = FeedbackItemForm(request.POST or None, instance=feedback_item)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.username = request.user
        obj.save()
        return redirect("feedback:index")
    return render(
        request,
        "feedback/edit_feedback_item_form.html",
        {"form": form, "feedback_item_id": feedback_item_id},
    )


@login_required
def delete_feedback_item(request, feedback_item_id):
    feedback_item = FeedbackItem.objects.get(pk=feedback_item_id)
    feedback_item.delete()
    messages.info(request, "Entry deleted")
    return redirect("feedback:index")
