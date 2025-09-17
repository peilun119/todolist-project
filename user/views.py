from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # django 預設就有內建的註冊表單
from django.contrib.auth.models import User  #  引用django 內建的使用者模型
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def user_register(request):
    message = ""  # 不管GET還是POST都要用到,要宣告在全域
    form = UserCreationForm()

    if request.method == "POST":
        print(request.POST)  #  終端機會顯示 註冊的資料

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 密碼不能少於8個字元,且兩次密碼必須相同
        if len(password1) < 8 or len(password2) < 8:
            message = "密碼不能少於8個字元!"
        elif password1 != password2:
            message = "兩次密碼不相同!"
        else:
            # 使用者名稱已存在
            if User.objects.filter(username=username):  #  如果有找到使用者的名稱
                message = "使用者名稱已存在!"
            else:
                User.objects.create_user(
                    username=username, password=password1
                ).save()  # 成功直接存檔
                message = "使用者註冊成功!"
                return redirect("user_login")

    return render(request, "user/register.html", {"form": form, "message": message})


# 登入畫面
def user_login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")  # get() 是取用template上input標籤的name
        password = request.POST.get("password")

        user = authenticate(
            request, username=username, password=password
        )  # authenticate 匹配資料
        if not user:
            message = "帳號或密碼錯誤!"
        else:
            login(request, user)  # 登入
            message = "登入成功!"
            return redirect("todolist")  # 登入導到新增代辦事項

    return render(request, "user/login.html", {"message": message})
