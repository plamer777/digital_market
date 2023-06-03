"""This file contains CBVs to render user entities"""
from rest_framework.generics import CreateAPIView
from django.conf import settings
from core.models import User
from core.serializers import UserCreateSerializer
# -------------------------------------------------------------------------


class UserCreateView(CreateAPIView):
    """This view is used to create a new user"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer: UserCreateSerializer) -> None:
        """This method was rewritten to create a hashed password
        :param serializer: A UserCreateSerializer instance
        """
        instance: User = serializer.save()
        instance.set_password(instance.password)
        instance.is_active = settings.NEW_USER_IS_STAFF
        instance.save()
