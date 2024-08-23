from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Asegúrate de importar el modelo de usuario que estás utilizando

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario  # Asegúrate de que está utilizando tu modelo personalizado
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user