from django.shortcuts import render,redirect
from .models import Review,ReviewImage
from .form import Review_form
from django.contrib.auth.decorators import login_required
# Create your views here.
def create(request):
    if request.method=="POST":
        createreq=Review_form(request.POST)
        photo_list=request.FILES.getlist("image[]")
        if createreq.is_valid():
            newreview=createreq.save(commit=False)
            newreview.save()
            for photo in photo_list:
                nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                nreviewimage.save()
        return redirect("reviews:index")
    else:
        form=Review_form()
        context={"form":form}
        return render(request,"reviews/create.html",context)
def update(request,review_pk):
    pass
def delete(request,review_pk):
    pass
def index(request):
    return render(request,"reviews/index.html")
def likes(request,review_pk):
    pass
def detail(request,review_pk):
    pass