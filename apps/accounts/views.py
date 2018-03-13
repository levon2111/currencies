# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.
from .models import Account
from .serializers import AccountSerializer
from core.mixins import AllMethodsViewSet


class AccountViewSet(AllMethodsViewSet):
    """
    CRUD endpoints for Account.
    """
    model_name = "Account"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
