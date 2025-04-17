from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title