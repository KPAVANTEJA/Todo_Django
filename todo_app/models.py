from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True)
    # task completion status
    completed = models.BooleanField(default=False)

    #creation time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title