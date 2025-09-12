# Django 預設的 form 表單
from django.forms import ModelForm

# 匯入模組套件
from .models import Todo


class TodoForm(ModelForm):
    # Meta -> 設定的概念
    class Meta:
        model = Todo
        # fields = "__all__"  # "__all__" 代表全部的物件
        fields = ["title", "text", "important"]
