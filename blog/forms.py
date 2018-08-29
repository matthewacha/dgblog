from django.forms import (
    EmailField,
    ModelForm,
    CharField,
    widgets,

)
from blog.models import Post

class PostForm(ModelForm):
    title = CharField(max_length=100, widget = widgets.TextInput(attrs={'class':'form-control'}))
    body = CharField(max_length=2000, widget =  widgets.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'body')