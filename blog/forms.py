from django import forms as f

from .models import Comment


class EmailPostForm(f.Form):
    name = f.CharField(max_length=25)
    email = f.EmailField()
    to = f.EmailField()
    comments = f.CharField(required=False, widget=f.Textarea)


class CommentForm(f.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']