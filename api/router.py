from rest_framework import routers
from .viewsets import EmployeeViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('employee', EmployeeViewSet)
