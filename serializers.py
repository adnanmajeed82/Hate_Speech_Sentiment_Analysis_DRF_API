# sentiment_analysis_app/serializers.py
from rest_framework import serializers
from .models import SentimentAnalysisResult

class SentimentAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentAnalysisResult
        fields = '__all__'
