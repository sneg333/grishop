from .models import Comment
from django import forms

'''форма комментария'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title_com', 'body_com']

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
