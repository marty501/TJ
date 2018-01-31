from django import forms
from tjapp.models import Post

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

#
#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('title', 'body',)
