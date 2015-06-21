from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "Jigar"
        instance.save()
        context = {
            "title": "Thank You"
        }
    return render(request, "home.html", context)

