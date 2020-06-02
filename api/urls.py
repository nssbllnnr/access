from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('personal', viewset=PersonalViewSet, basename='Personal')
router.register('employee', viewset=EmployeeViewSet, basename='Employee')
router.register('device', viewset=DeviceViewSet, basename='Device')
# router.register('discs', viewset=DiscViewSet, basename='Диски')

urlpatterns = router.urls