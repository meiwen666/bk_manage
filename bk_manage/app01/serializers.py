from rest_framework import  serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cron
        fields = "__all__"



class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列表类
    """
    class Meta:
        model = User
        fields = "__all__"



















# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "username,email"










# class PathSerializer(serializers.ModelSerializer):
#      class Meta:
#          model = Path
#          fields = "__all__"

