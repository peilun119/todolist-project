# Serializer 是模型與JSON 之間的橋樑，負責資料格式轉換。
from rest_framework import serializers
from todo.models import Todo  # 將todo 的 models 引用進來作序列化
from django.contrib.auth.models import User


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"  # Todo的所有欄位


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # Todo的所有欄位
