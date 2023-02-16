from django.db import models
from django.conf import settings
# User = settings.AUTH_USER_MODEL
from account.models import User

class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    isComplete=models.BooleanField(default=False)
    deadline=models.DateTimeField()
    user=models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title