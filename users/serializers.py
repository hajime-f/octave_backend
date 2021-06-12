from rest_framework.serializers import ModelSerializer
from users.models import User
from django.contrib.auth.hashers import make_password # 追加

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    # createメソッドをオーバライド
    def create(self, validated_data):
        password = validated_data.get('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        return super().create(validated_data);
