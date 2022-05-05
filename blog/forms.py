from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['author','title','content','image']


        widgets={
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
       



        }
       