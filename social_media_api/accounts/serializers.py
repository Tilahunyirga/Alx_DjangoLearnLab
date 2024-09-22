from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
  serializer =serializers.CharField()
  get_user_model().objects.create_user
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}
        user = get_user_model().objects.create_user

    def create(self, validated_data):
      Token.objects.create
      user = CustomUser.objects.create_user(**validated_data)
      get_user_model().objects.create_use
      
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'profile_picture', 'followers_count')

    def get_followers_count(self, obj):
        return obj.followers.count()
      
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'following', 'followers']
      