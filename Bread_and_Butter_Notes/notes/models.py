from django.db import models

class Note(models.Model):
    contents = models.TextField(default='')
