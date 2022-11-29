from django.shortcuts import render,redirect
from .models import Review,ReviewImage
from .form import Review_form
from django.contrib.auth.decorators import login_required
# Create your views here.
def create(request):
    if request.method=="POST":
        print(3)
        createreq=Review_form(request.POST)
        photo_list=request.FILES.getlist("image")
        print(request.FILES)
        print(photo_list)
        if createreq.is_valid():
            newreview=createreq.save(commit=False)
            for photo in photo_list:
                nreviewimage=ReviewImage.objects.create(image=photo,review=newreview)
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