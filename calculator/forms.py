from django import forms
from .models import YourModel  # Replace YourModel with the actual model name

class AddNumbersForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['num1', 'num2']

