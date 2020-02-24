from rest_framework import serializers
from structure.models import Employee, User


def str_to_int(val):
    try:
        int(val)
        return True
    except:
        return False


def validate_nic(nic):
    nic_len = len(nic)
    if nic_len not in [10, 12]:
        return False, 'invalid length'

    if nic_len == 10 and nic[-1].lower() != 'v':
        return False, 'invalid last letter'
    elif nic_len == 12 and not str_to_int(nic):
        return False, 'enter valid integers'

    return True, None


class EmployeeSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(required=False)
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
    retype_password = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, attrs):
        command, count = '-', 204
        print(command * count)
        test = attrs
        print(test)
        print(type(test))
        print(dir(test))
        print(command * count)
        # check whether user available
        username = attrs.get('username')
        user = User.objects.filter(username=username)
        if user.exists():
            message = f'username {username} already exists'
            raise serializers.ValidationError({'username': message})

        # check whether password match
        password = attrs.get('password')
        retype_password = attrs.get('retype_password')
        if password != retype_password:
            message = 'password doesnt match'
            raise serializers.ValidationError({
                'password': message,
                'retype_password': message
            })

        # validate NIC number
        nic_number = attrs.get('nic_number')
        status, message = validate_nic(nic_number)
        if not status:
            raise serializers.ValidationError({'nic_number': message})

        return attrs

    def get_user(self, instance):
        username = instance.get('username')
        password = instance.get('password')
        user = User.objects.create_user(username=username, password=password)
        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class EmployeeSerializers_new(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Employee
        fields = '__all__'
