from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    iscompleted = models.BooleanField(default=False)
    deadline = models.DateField()
