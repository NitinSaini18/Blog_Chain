from django import forms
from .models import Blog,Comment

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
