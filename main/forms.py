from django import forms

from .models import NewsLater , UserReqester , CommentModel

# Comment form 
class Comment(forms.ModelForm):
    class Meta:
        model =CommentModel
        fields = ['name' , 'email', 'comment']


# SingUp form 
class SignUp(forms.ModelForm):
    class Meta:
        model = UserReqester
        fields = ['username' , 'password' , 'email']
    

class NewsLatterForm(forms.ModelForm):
    class Meta:
        model = NewsLater
        fields = ("name", "email")