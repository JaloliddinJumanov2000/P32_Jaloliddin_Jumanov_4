from django import forms
from .models import Suggestion
from django.core.validators import MaxLengthValidator

class SuggestionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, validators=[MaxLengthValidator(1000)])

    class Meta:
        model = Suggestion
        fields = ['title', 'content', 'status']
