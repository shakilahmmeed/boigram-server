from rest_framework.serializers import ModelSerializer

from account.models import User, Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')
        username = validated_data.pop('username')
        email = validated_data.pop('email', '')
        password = validated_data.pop('password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password)
        return user


class ProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
