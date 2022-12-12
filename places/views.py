from .forms import PlaceForm
from .models import Place
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from reviews.models import Review


def index(request):
    places = Place.objects.order_by("-pk")
    context = {
        "places": places,
    }

    return render(request, "places/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        places_form = PlaceForm(request.POST, request.FILES)
        if places_form.is_valid():
            place = places_form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect("places:index")
    else:
        place_form = PlaceForm()
    context = {
        "place_form": place_form,
    }
    return render(request, "places/create.html", context)


def detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    context = {
        "place": place,
    }

    response = render(request, "places/detail.html", context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get("hitboard", "_")

    if f"_{pk}_" not in cookie_value:
        cookie_value += f"_{pk}_"
        response.set_cookie(
            "hitboard", value=cookie_value, max_age=max_age, httponly=True
        )
        place.hits += 1
        place.save()

    return response


@login_required
def update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    # if request.user == place.user:
    if request.method == "POST":
        place_form = PlaceForm(request.POST, request.FILES, instance=place)
        if place_form.is_valid():
            place = place_form.save(commit=False)
            place.save()
            return redirect("places:detail", place.pk)
    else:
        place_form = PlaceForm(instance=place)
    context = {
        "place_form": place_form,
    }
    return render(request, "places/update.html", context)


@login_required
def delete(request, pk):
    place = Place.objects.get(pk=pk)
    place.delete()
    return redirect("places:index")


@login_required
def like(request, pk):
    print(request.POST)
    if request.user.is_authenticated:
        place = Place.objects.get(pk=pk)
        if place.like_users.filter(pk=request.user.pk).exists():
            place.like_users.remove(request.user)
            is_liked = False
        else:
            place.like_users.add(request.user)
            is_liked = True
    else:
        return redirect("places:detail", pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": place.like_users.count(),
        }
    )

# 스키장별 리뷰보기
def place_reviews(request, pk):
    # 해당 스키장
    place = Place.objects.get(pk=pk)
    # place의 리뷰들 
    reviews = Review.objects.filter(place=place).order_by("-updated_at")
    return render(request, 'places/place_reviews.html', {'reviews':reviews, 'place':place})