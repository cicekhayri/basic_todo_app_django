from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
