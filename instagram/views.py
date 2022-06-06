from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostImage,EditProfile,UpdateProfile,CommentForm,Likes,FormFollow
from .models import Image,Profile,Comments,Followers
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def stories(request):
    try:
        current_user=request.user.id
        images=Image.objects.all()
        profile_image=Profile.objects.filter(userId=current_user)
        profile=profile_image.reverse()[0:1]
        users=User.objects.all().exclude(id=request.user.id)
        comments=Comments.objects.all()
        #comments
    except Exception as e:
        raise Http404()
