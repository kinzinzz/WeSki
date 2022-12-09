from django.shortcuts import render,redirect
from .models import Review,ReviewImage
from .form import Review_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from places.models import Place
from datetime import timedelta,datetime
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
# Create your views here.
@login_required
def create(request):
    if request.method=="POST":
        createreq=Review_form(request.POST)
        photo_list=request.FILES.getlist("image[]")
        if createreq.is_valid():
            newreview=createreq.save(commit=False)
            newreview.user=request.user
            place_pk=newreview.place.pk
            newreview.save()
            for photo in photo_list:
                nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                nreviewimage.save()
        return redirect("places:place_reviews",place_pk)
    else:
        form=Review_form()
        context={"Review_form":form}
        httpobject=render(request,"reviews/create.html",context)
        return httpobject

@login_required
def update(request,review_pk):
    old_review=Review.objects.get(pk=review_pk)
    if request.user.pk==old_review.user.pk:
        if request.method=="POST":
            createreq=Review_form(request.POST,instance=old_review)
            photo_list=request.FILES.getlist("image[]")
            del_photo_list=request.POST.getlist("dellist")
            if createreq.is_valid():
                newreview=createreq.save(commit=False)
                newreview.user=request.user
                place_pk=newreview.place.pk
                newreview.save()
                for photo in photo_list:
                    nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                    nreviewimage.save()
                for delphoto in del_photo_list:
                    delreviewimage=ReviewImage.objects.get(pk=delphoto)
                    delreviewimage.delete()
            return redirect("places:place_reviews",place_pk)
        else:
            form=Review_form(instance=old_review)
            photo=ReviewImage.objects.filter(review=old_review.pk)
            context={"form":form,"photos":photo}
            return render(request,"reviews/update.html",context)
    else:
        return redirect("reviews:index")
@login_required
def delete(request,review_pk):
    old_review=Review.objects.get(pk=review_pk)
    place_pk=old_review.place.pk
    if(request.user.pk==old_review.user.pk):
        if(request.method=="POST"):
            old_review.delete()
    return redirect("places:place_reviews",place_pk)
@require_http_methods(["POST"])
def likes(request,review_pk):
    if request.user.is_authenticated:
        print(review_pk)
        user=request.user.pk
        review=Review.objects.get(pk=review_pk)
        if review.likes.filter(pk=user).exists():
            review.likes.remove(user)
            review.likes_num=review.likes_num-1
            review.save()
            Is_liked=False
        else:
            review.likes.add(user)
            review.likes_num=review.likes_num+1
            review.save()
            Is_liked=True
        context={'is_liked':Is_liked,'likesnum':review.likes_num}
    return JsonResponse(context)
@login_required
def detail(request,review_pk):
    reviewobject=Review.objects.get(pk=review_pk)
    Writerobject=get_user_model().objects.get(pk=reviewobject.user.pk)
    reviewplaceobject=Place.objects.get(pk=reviewobject.place.pk)
    context={"Review":reviewobject,"Place":reviewplaceobject,"User":Writerobject}
    return render(request,"reviews/detail.html",context)
@login_required
def image_add(request,review_pk):
    reviewobj=Review.objects.get(pk=review_pk)
    if request.method=="POST" and request.user==reviewobj.user:
        photo_list=request.FILES.getlist("image[]")
        for photo in photo_list:
            nreviewimage=ReviewImage.objects.create(review=reviewobj,image=photo)
            nreviewimage.save()
    goto="reviews:detail"
    if request.COOKIES.get("from"):
        goto=request.COOKIES.get("from")
    return redirect(goto,review_pk)
@login_required
def image_delete(request,review_pk,reviewimage_pk):
    reviewobj=Review.objects.get(pk=review_pk)
    if request.method=="POST" and request.user==reviewobj.user:
        delobj=ReviewImage.objects.get(pk=reviewimage_pk)
        delobj.delete()
    return redirect("reviews:detail",review_pk)
