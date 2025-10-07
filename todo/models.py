from django.db import models

# Create your models here.
class Task(models.Model):
    session_key = models.CharField(max_length = 40, db_index = True)
    task = models.CharField(max_length = 250)
    is_completed = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
