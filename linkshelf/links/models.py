from django.db import models

class Link(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.url)

