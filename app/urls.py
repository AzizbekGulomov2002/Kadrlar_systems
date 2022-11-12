from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import Hodim_haqidaViewSet, HodimlarViewSet,BolimlarviewSet,QarindoshlikViewSet

router = DefaultRouter()
router.register('bolimlar',BolimlarviewSet)
router.register('hodimlar',HodimlarViewSet)
router.register('hodim_haqida',Hodim_haqidaViewSet)
router.register('qarindoshlik',QarindoshlikViewSet)


urlpatterns = [
    path('', include(router.urls))
]