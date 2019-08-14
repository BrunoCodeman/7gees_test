from django.db import models

class ShortenedUrlModel(models.Model):
    original_url = models.TextField()
    shortened_url = models.TextField()



