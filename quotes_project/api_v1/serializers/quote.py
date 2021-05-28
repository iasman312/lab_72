from rest_framework import serializers

from api_v1.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'email', 'rating', 'status', 'created_at')
        read_only_fields = ('author', 'id', 'rating')