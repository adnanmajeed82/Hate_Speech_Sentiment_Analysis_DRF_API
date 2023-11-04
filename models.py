# sentiment_analysis_app/models.py
from django.db import models

class SentimentAnalysisResult(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)
    confidence = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.text
