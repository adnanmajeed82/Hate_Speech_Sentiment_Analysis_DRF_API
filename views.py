# sentiment_analysis_app/views.py
from rest_framework import generics
from rest_framework.response import Response
from transformers import pipeline
from .models import SentimentAnalysisResult
from .serializers import SentimentAnalysisResultSerializer

class SentimentAnalysisView(generics.CreateAPIView):
    queryset = SentimentAnalysisResult.objects.all()
    serializer_class = SentimentAnalysisResultSerializer

    def create(self, request, *args, **kwargs):
        text = request.data.get('text')

        # Perform sentiment analysis using a pre-trained model from Transformers
        sentiment_analysis = pipeline('sentiment-analysis')
        results = sentiment_analysis(text)

        # Extract the sentiment label and confidence score
        sentiment_label = results[0]['label']
        confidence = results[0]['score']

        analysis_result = SentimentAnalysisResult.objects.create(
            text=text,
            sentiment=sentiment_label,
            confidence=confidence
        )

        serializer = SentimentAnalysisResultSerializer(analysis_result)
        return Response(serializer.data)
