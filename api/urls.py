from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('personal', viewset=PersonalViewSet, basename='Personal')
router.register('employee', viewset=EmployeeViewSet, basename='Employee')
router.register('device', viewset=DeviceViewSet, basename='Device')
router.register('access', viewset=AccessViewSet, basename='Access')
router.register('history', viewset=HistoryViewSet, basename='History')

urlpatterns = router.urls