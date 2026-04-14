from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)   # ✅ NEW FIELD
    created_at = models.DateTimeField(auto_now_add=True)