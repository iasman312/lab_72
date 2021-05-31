from django.urls import include, path

from api_v1.views import QuoteView, QuoteDetailView, index, get_token_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v1'

article_urls = [
    path('', index, name='index'),
    path('quote/', QuoteView.as_view(), name='quotes'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote')
]

urlpatterns = [
    path('', include(article_urls)),
    path('get_token/', get_token_view),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

