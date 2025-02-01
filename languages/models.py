from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
