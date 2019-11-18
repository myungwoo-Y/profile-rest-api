from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'password')
        # 비밀번호는 다시 쓰기만 가능하도록 설정
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                # 비밀번호를 별로 표현되도록
                'style' : {'input_type' : 'password'}
            }
        }
    
    # serializer 에서도 create 제공하지만
    # 이것은 password로 plain text를 요구하므로 이미 암호화 된 password는 사용부가능
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}