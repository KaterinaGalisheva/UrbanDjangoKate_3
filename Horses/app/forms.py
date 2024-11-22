from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.IntegerField(
        max_value=100,
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={'placeholder': 'Возраст'})
    )