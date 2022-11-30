from django.shortcuts import render,redirect
from .models import Review,ReviewImage
from .form import Review_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.
@login_required(login_url="accounts/login")
def create(request):
    if request.method=="POST":
        createreq=Review_form(request.POST)
        photo_list=request.FILES.getlist("image[]")
        if createreq.is_valid():
            newreview=createreq.save(commit=False)
            newreview.user=request.user
            newreview.save()
            for photo in photo_list:
                nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                nreviewimage.save()
        return redirect("reviews:index")
    else:
        form=Review_form()
        context={"form":form}
        return render(request,"reviews/create.html",context)
@login_required(login_url="accounts/login")
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
                newreview.save()
                for photo in photo_list:
                    nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                    nreviewimage.save()
                for delphoto in del_photo_list:
                    delreviewimage=ReviewImage.objects.get(pk=delphoto)
                    delreviewimage.delete()
            return redirect("reviews:index")
        else:
            form=Review_form(instance=old_review)
            photo=ReviewImage.objects.filter(review=old_review)
            context={"form":form,"photos":photo}
            return render(request,"reviews/update.html",context)
    else:
        return redirect("reviews:index")
@login_required(login_url="accounts/login")
def delete(request,review_pk):
    old_review=Review.objects.get(pk=review_pk)
    if(request.user.pk==old_review.user.pk):
        if(request.method=="POST"):
            old_review.delete()
    return redirect("reviews:index")
def index(request):
    reviewobject=Review.objects.order_by("-pk")
    context={"Reviews":reviewobject}
    return render(request,"reviews/index.html",context)
def likes(request,review_pk):
    pass
def detail(request,review_pk):
    reviewobject=Review.objects.get(pk=review_pk)
    Writer=reviewobject.user
    print(Writer.username)
    context={"Review":reviewobject,"Review_Writer":Writer
    }
    return render(request,"reviews/detail.html",context)