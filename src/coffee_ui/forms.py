from django import forms


class FormPosition(forms.Form):
    name = forms.CharField(label='name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='price', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.IntegerField(label='category', widget=forms.NumberInput(attrs={'class': 'form-control'}))


class FormOrder(forms.Form):
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    position_id = forms.CharField(label='position_id', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='price', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    seller = forms.IntegerField(label='seller', widget=forms.NumberInput(attrs={'class': 'form-control'}))


class DeleteAPI(forms.Form):
    id = forms.IntegerField(label='id', widget=forms.NumberInput(attrs={'class': 'form-control'}))