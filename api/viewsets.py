from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import EmployeeSerializers, EmployeeSerializers_new
from structure.models import Employee, User


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def create(self, request, *args, **kwargs):
        # TODO: must delete below two lines
        Employee.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        ser = EmployeeSerializers(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        data.pop('username', None)
        data.pop('password', None)
        data.pop('retype_password', None)
        data['photo'] = request.data.get('photo')
        obj = Employee.objects.create(**data)
        ser = EmployeeSerializers_new(obj)
        return Response(ser.data)
