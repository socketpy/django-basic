from django.db import models

# Create your models here.
class Todolist(models.Model):
    #create field
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)