from django.shortcuts import render
from .serializers import TodoSerializers, UserSerializers
from rest_framework import viewsets  # 引用 viewsets 模組
from todo.models import Todo
from django.contrib.auth.models import User

# Create your views here.


# ViewSet 可自動產出「查詢、新增、更新、刪除」行為。
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializers

    # get_queryset() 控制查詢哪些資料。
    def get_queryset(self):
        return Todo.objects.all().order_by("-created")


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers

    # get_queryset() 控制查詢哪些資料。
    def get_queryset(self):
        return User.objects.all().order_by("-date_joined")
