from .models import PerevalAdded
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import PerevalSerializer
from rest_framework.views import APIView


class PerevalViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
