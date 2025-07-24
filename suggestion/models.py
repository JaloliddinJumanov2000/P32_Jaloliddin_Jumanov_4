from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator


class Suggestion(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('approved', 'Tasdiqlangan'),
        ('rejected', 'Rad etilgan'),
    ]

    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(
        validators=[MaxLengthValidator(1000)],
        verbose_name="Matn"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Holat"
    )

    class Meta:
        verbose_name = "Fikr va Taklif"
        verbose_name_plural = "Fikr va Takliflar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_short_content(self):
        return self.content[:100] + "..." if len(self.content) > 100 else self.content
