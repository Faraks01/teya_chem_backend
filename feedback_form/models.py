from django.db import models


class FeedbackForm(models.Model):
    full_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=254)
    comment = models.CharField(max_length=800, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    attachment_file = models.FileField()
