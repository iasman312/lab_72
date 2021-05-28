from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.models import Quote, Rating
from api_v1.serializers import QuoteSerializer
from api_v1.serializers.quote import UpdateSerializer
from api_v1.views.permissions import HasPermission


class QuoteView(APIView):
    permission_classes = [HasPermission]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.has_perms('api_v1.view_all'):
            quotes = Quote.objects.all()
        else:
            quotes = Quote.objects.filter(status="Moderated")
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
        self.check_object_permissions(self.request, quote)
        response_data = QuoteSerializer(quote, many=False).data

        return Response(data=response_data)

    def put(self, request, pk, *args, **kwargs):
        quote = Quote.objects.get(pk=pk)
        self.check_object_permissions(self.request, quote)
        quote_data = request.data
        serializer = UpdateSerializer(instance=quote, data=quote_data)
        serializer.is_valid(raise_exception=True)
        updated_quote = serializer.save()
        return Response({'id': updated_quote.id})

    def delete(self, request, pk, *args, **kwargs):
        quote = Quote.objects.get(pk=pk)
        self.check_object_permissions(self.request, quote)
        quote.delete()
        return Response({'success': 'Successfully deleted'})


class RatingView(APIView):
    def post(self, request, *args, **kwargs):
        pass

