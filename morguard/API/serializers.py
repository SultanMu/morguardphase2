from rest_framework import serializers
from .models import User
class IndexSerializer(serializers.Serializer):
    files = serializers.CharField()
    uuid4 = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","email","password"]
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def create(self,validated_data):
        password = validated_data.pop("password",None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class ReportSerializer(serializers.Serializer):
    file_name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    company = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    created_date = serializers.DateField(format="%Y-%m-%d")
    next_asses_date = serializers.DateField(format="%Y-%m-%d")
    summary = serializers.CharField(max_length=1000)
    flag = serializers.BooleanField()