from rest_framework import serializers

from djongo_app.models import Tag, ArticleEntry


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleEntry
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
