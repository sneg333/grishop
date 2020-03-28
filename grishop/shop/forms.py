from .models import Comments
from django import forms

# форма комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['title_com', 'comment_email', 'body']