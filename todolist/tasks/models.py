from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


def in_10_days():
    return timezone.now() + timedelta(days=10)


class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=in_10_days)
    priority = models.PositiveSmallIntegerField(validators=[
                                                        MinValueValidator(1),
                                                        MaxValueValidator(10)
                                                    ])

    def __str__(self):
        return self.title
