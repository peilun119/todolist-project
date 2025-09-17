"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

# 直接引用自己資料夾的views.py
from .views import create_todo, view_todo, delete_todo, todolist

# 從todolist 複製url.py過來修改
# 留下todo需要的首頁/新增/修改/刪除 四個功能
urlpatterns = [
    path("delete-todo/<int:id>", delete_todo, name="delete-todo"),
    path("create-todo/", create_todo, name="create-todo"),
    path("todo/<int:id>", view_todo, name="view-todo"),
    path("", todolist, name="todolist"),
]
