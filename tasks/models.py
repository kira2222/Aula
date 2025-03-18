from django.db import models

# Create your models here.

class TaskPriorityTextChoices(models.TextChoices):
    ALTA = "Alta"
    MEDIA = "Media"
    BAJA = "Baja"


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_limit = models.DateTimeField(null=True, blank=True)
    priot = models.CharField(max_length=20,choices=TaskPriorityTextChoices.choices)

    def __str__(self):
        return self.title