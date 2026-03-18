from .models import AuthorModel,QuoteModel
from rest_framework import serializers



class quoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteModel
        fields = '__all__'



class authorSerializer(serializers.ModelSerializer):
    quotes = quoteSerializer(many=True,read_only=True)
    class Meta:
        model = AuthorModel
        fields = '__all__'