from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.

def home(request):
    my_form = RawFeedbackForm()
    if request.method == "POST":
        my_form = RawFeedbackForm(request.POST)
        if my_form.is_valid():
            print('Kaweesi data is cleaned ',)
            Feedback.objects.create(**my_form.cleaned_data)
            my_form = RawFeedbackForm()
        else:
            print('Kaweesi, they was an Error')
    context = {
        "form": my_form
    }
    return render(request, 'home.html', context)


def cv(request):
    context = {}
    return render(request, 'cv.html', context)
