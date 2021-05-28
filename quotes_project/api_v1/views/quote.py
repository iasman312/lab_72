import json

from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.models import Quote
from api_v1.serializers import QuoteSerializer


class QuoteView(APIView):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        response_data = QuoteSerializer(quotes, many=True).data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        quote_data = request.data
        serializer = QuoteSerializer(data=quote_data)
        serializer.is_valid(raise_exception=True)
        quote = serializer.save()
        return Response({'id': quote.id})


class QuoteDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        quote = Quote.objects.get(pk=pk)
        response_data = QuoteSerializer(quote, many=False).data

        return Response(data=response_data)

    def put(self, request, pk, *args, **kwargs):
        quote = Quote.objects.get(pk=pk)
        quote_data = request.data
        serializer = QuoteSerializer(instance=quote, data=quote_data)
        serializer.is_valid(raise_exception=True)
        updated_quote = serializer.save()
        return Response({'id': updated_quote.id})

    def delete(self, request, pk, *args, **kwargs):
        quote = Quote.objects.get(pk=pk)
        quote.delete()
        return Response({'success': 'Successfully deleted'})