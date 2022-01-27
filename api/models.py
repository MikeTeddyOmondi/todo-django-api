from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
      
    def __str__(self):
        return str(self.title)
        