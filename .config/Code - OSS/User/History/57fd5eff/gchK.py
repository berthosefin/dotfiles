from django import forms
from .models import Person, Student


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
    
        if email and password:
            result = Person.objects.filter(password=password, email=email)
            if len(result) != 1:
                raise forms.ValidationError("Addresse de courriel ou mot de passe erroné(e).")
        
        return cleaned_data


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('friends',)