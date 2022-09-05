from django.db import models


# Create your models here.
class Todo_App(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    Task_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_done =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
