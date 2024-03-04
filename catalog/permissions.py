from rest_framework.permissions import BasePermission

from authentication.models import User


class BookCreatePermission(BasePermission):
    message = "Adding book for non Admin user not allowed."

    def has_permission(self, request, view):
        if request.user.role == User.ADMIN:
            return True
        return False


