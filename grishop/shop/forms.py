from .models import RaitingStar, Raiting, Comment
from django import forms

'''форма комментария'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title_com', 'body_com']

class RatingForm(forms.ModelForm):
    """форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RaitingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Raiting
        fields = ("star", )

        """из папки cart"""
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

'''форма комментария'''
class CommentForm(forms.ModelForm):# commentarii
    class Meta:
        model = Comment
        fields = ['title_com', 'body_com', 'rate']
