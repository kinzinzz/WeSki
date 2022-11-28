from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as user_login

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            user_login(request, user)
            return redirect("reviews:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }

    return render(request, "accounts/signup.html", context)
