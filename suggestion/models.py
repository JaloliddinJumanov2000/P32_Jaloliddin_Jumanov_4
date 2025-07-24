from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model
User = get_user_model()

class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Text',config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
