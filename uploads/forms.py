from django import forms


class DNAOverviewForm(forms.Form):
    image = forms.ImageField(
        label="Select a Image file",
    )