"""This file contains permissions for supplier application"""
from django.http import HttpRequest
from rest_framework.permissions import BasePermission
# --------------------------------------------------------------------------


class IsStaffPermission(BasePermission):
    """This permission restricts access to the API for users without
    is_staff status"""
    def has_permission(self, request: HttpRequest, view) -> bool:
        try:
            if request.user.is_staff:
                return True

            return False

        except Exception:
            return False
