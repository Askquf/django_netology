from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

class CreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.method, obj.creator, request.user)
        if request.method == 'GET':
            return True
        else:
            return obj.creator == request.user


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), CreatorOrReadOnly()]
        return []

    def get_queryset(self):
        return Advertisement.objects.exclude(status='DRAFT')