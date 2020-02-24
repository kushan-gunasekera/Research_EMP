from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .serializers import EmployeeSerializers, EmployeeSerializers_new
from structure.models import Employee, User


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def create(self, request, *args, **kwargs):
        # TODO: must delete below two lines
        # return Response({'a': 'a'})
        Employee.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        ser = EmployeeSerializers(data=request.data)
        # ser.is_valid(raise_exception=True)
        if not ser.is_valid():
            command, count = '*', 204
            print(command * count)
            test = ser.errors
            print(test)
            print(type(test))
            print(dir(test))
            print(command * count)
            raise serializers.ValidationError(ser.errors)
        data = ser.data
        data.pop('username', None)
        data.pop('password', None)
        data.pop('retype_password', None)
        data['photo'] = request.data.get('photo')
        obj = Employee.objects.create(**data)
        ser = EmployeeSerializers_new(obj)
        return Response(ser.data)

    # def list(self, request, *args, **kwargs):
    #     return Response({'a': 'a'})
