from django.db import models


class HeaderChapter(models.Model):
    title = models.CharField(max_length=90, null=False, unique=True)
    description = models.TextField()
    link = models.URLField(null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.description}"


