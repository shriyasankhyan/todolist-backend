from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
# class Todo(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=200)
#     iscompleted = models.BooleanField(default=False)
#     deadline = models.DateField()
class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    isComplete=models.BooleanField(default=False)
    deadline=models.DateTimeField()

    def __str__(self):
        return self.title
    class Meta:
        ordering=['isComplete']