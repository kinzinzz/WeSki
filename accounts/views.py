from django.shortcuts import render, redirect
from .forms import SignupForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    login as user_login,
    logout as user_logout,
    get_user_model,
)
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            user_login(request, user)
            return redirect("places:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect(request.GET.get("next") or "places:index")
    else:
        form = AuthenticationForm()
    context = {"forms": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    user_logout(request)
    return redirect("places:index")

@login_required
def detail(request, user_pk):
    customer = get_user_model().objects.get(pk=user_pk)
    context = {
        "customer": customer,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def update(request, user_pk):
    infos = get_user_model().objects.get(pk=user_pk)
    customer = infos
    if request.method == "POST":
        forms = ChangeUserForm(request.POST, request.FILES, instance=infos)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:detail", user_pk)
    else:
        forms = ChangeUserForm(instance=infos)
    context = {
        "forms": forms,
        "customer": customer,
    }
    return render(request, "accounts/update.html", context)


@login_required
def delete(request, user_pk):
    customer = get_user_model().objects.get(pk=user_pk)
    if customer.pk == request.user.pk:
        customer.delete()
    return redirect("places:index")