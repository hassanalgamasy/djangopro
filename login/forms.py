from django import forms
class LoginForm(forms.Form):
    username= forms.CharField(
        label="اسم المستخدم او رقم الهاتف ",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'ادخل اسم المستخدم او الموبايل'
        })
    )
    password=forms.CharField(
        label='كلمه السر ؟',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'ادخل كلمه السر'
        })
    )