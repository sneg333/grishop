from .models import RaitingStar, Raiting
from django import forms

# форма комментария
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['title_com', 'comment_email', 'body']

class RatingForms(forms.ModelForm):
    """форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RaitingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Raiting
        fields = ("star", )