from .models import Names
from django.forms import ModelForm, TextInput


class NamesForm(ModelForm):
    class Meta:
        model = Names
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ваше имя'
            })
        }
