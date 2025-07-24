from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget
from Suggestion.models import Suggestion


class SuggestionForms(ModelForm):
    objects = None

    class Meta:
        model = Suggestion
        fields = ('title', 'content', 'created_at', 'updated_at', 'user','status')
        widgets = {
            'content': CKEditor5Widget(config_name='extends'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False

