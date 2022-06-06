from . models import Image,Profile,Comments,Followers
from django import forms

class PostImage(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId','profile']
