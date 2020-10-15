from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields= ('title','author','text')
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'pform','type':'hidden'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name','text')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','value':'','id':'cform','type':'hidden'})
        }
