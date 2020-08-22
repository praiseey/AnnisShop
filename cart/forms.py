from django import forms


PRODUCT_QUANTITY_CHOICES = [(qty, str(qty)) for qty in range(1, 21)]


class AddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(widget=forms.HiddenInput)
