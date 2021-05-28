from django.urls import include, path

from api_v1.views import QuoteView, QuoteDetailView

app_name = 'api_v1'

article_urls = [
    path('', QuoteView.as_view(), name='articles'),
    path('<int:pk>/', QuoteDetailView.as_view(), name='article')
]

urlpatterns = [
    path('quotes/', include(article_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

