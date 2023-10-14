from rest_framework.permissions import BasePermission

class CreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return obj.creator == request.user

