from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(label='Телефон', max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
