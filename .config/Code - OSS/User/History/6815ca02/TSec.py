from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
    
        if email and password:
            if password != 'passtest' or email != 'test@mail.test':
                raise forms.ValidationError("Addresse de courriel ou mot de passe erroné.")
        
        return cleaned_data