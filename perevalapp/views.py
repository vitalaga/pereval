from .models import PerevalAdded, Users
from .serializers import (
    PerevalSerializer, PerevalSubmitDataSerializer, PerevalSubmitDataUpdateSerializer, PerevalSubmitDataListSerializer
)

from rest_framework import mixins, generics, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response


class PerevalViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


class SubmitDataListView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = PerevalSubmitDataListSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            return self.queryset.filter(user__email=email)
        return self.queryset.none()


class SubmitDataDetailView(RetrieveAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSubmitDataSerializer


class SubmitDataUpdateView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = PerevalSubmitDataUpdateSerializer

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()

        if submit_data.status != 'new':
            message = "Статус 'new' не соответствует. Данные отредактировать не получится."
            return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.perform_update(serializer)

        return Response({'state': 1})

