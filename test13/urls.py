from django.urls import path
from rest_framework.routers import DefaultRouter

from test13.views import *


router = DefaultRouter()
router.register('userns', UserNViewSet)


urlpatterns = [
    path('products/', ProductsViewSet.as_view())
] + router.urls
