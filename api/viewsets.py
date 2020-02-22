from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import EmployeeSerializers, CustomEmployeeSerializers
from structure.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def create(self, request, *args, **kwargs):
        data = CustomEmployeeSerializers(data=request.data)
        data.is_valid(raise_exception=True)
        return Response('ok')
