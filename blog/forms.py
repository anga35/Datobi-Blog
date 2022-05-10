from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['title','content','image']


        widgets={
            
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
       



        }
       