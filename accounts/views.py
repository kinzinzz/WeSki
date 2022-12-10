from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    login as user_login,
    logout as user_logout,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from places.models import Place
from .models import OrderTransaction
# 카카오

import os





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
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(form.is_valid())
        if form.is_valid():
            user_login(request, form.get_user())
        
            # id = request.POST.get("id")
            # password = request.POST.get("password")
            
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
    places = Place.objects.order_by('-pk')
    customer = get_object_or_404(get_user_model(), pk=user_pk)
    order_place_ids = OrderTransaction.objects.filter(user=customer).values_list('place', flat=True).distinct()
    order_transactions = []
    for id in order_place_ids:
        order_transactions.append(Place.objects.get(pk=id))
    # customer = get_user_model().objects.get(pk=user_pk)
    # review_pg = request.GET.get("reviewpage")

    
    # customer_rv = customer.review_set.all()
    # Paginator(분할될 객체, 페이지마다 넣을 객체수)
    # review_data = Paginator(customer_rv, 5)
    # review_page = review_data.get_page(review_pg)

    
    reviews = customer.review_set.order_by('-pk')
    review_page = request.GET.get('review_page', '1')
    review_paginator = Paginator(reviews, 5)
    review_page_obj = review_paginator.get_page(review_page)

    context = {
        "places": places,
        "order_transactions": order_transactions,
        "customer": customer,
        # "review_page": review_page,
        "reviews": review_page_obj,

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
def deletemsg(request, user_pk):
    customer = get_user_model().objects.get(pk=user_pk)
    context = {
        'customer': customer,
    }
    return render(request, "accounts/deletemsg.html", context)

@login_required
def delete(request, user_pk):
    customer = get_user_model().objects.get(pk=user_pk)
    if customer.pk == request.user.pk:
        customer.delete()
    return redirect("places:index")

