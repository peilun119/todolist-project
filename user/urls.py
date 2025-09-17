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
from .views import user_register, user_login

# 從todo 複製url.py過來修改
urlpatterns = [
    # 跟todolist的url.py路徑user/合起來就是正確路徑user/register
    path("register/", user_register, name="user_register"),
    path("login/", user_login, name="user_login"),
]
