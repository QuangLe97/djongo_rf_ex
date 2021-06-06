from django.urls import include, path
from rest_framework import routers

from djongo_app.views import ArticleViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagViewSet)
serializer_url_pattern = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
