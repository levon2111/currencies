# Native Python Modules.

# External Modules.
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

# Django Modules.
from django.conf.urls import url, include
from django.contrib import admin

# Project Modules.
from apps.accounts.views import AccountViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', get_swagger_view(title='REST API Example')),
]
