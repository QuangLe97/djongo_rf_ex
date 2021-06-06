# Create your views here.
from rest_framework import viewsets

from djongo_app.models import Tag, ArticleEntry
from djongo_app.serializers import ArticleSerializer, TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = ArticleEntry.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
