from django import forms


class OrderForms(forms.Form):
    in_sum = forms.IntegerField(label='Внесённая сумма:', widget=forms.NumberInput(attrs={'class': 'form-control'}))
