from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
# 函式定要帶參數request
def index(request):

    return HttpResponse("<h1>Hello Django!</h1>")


# 練習新增一個books route
def books(resquest):
    my_books = {1: "Python", 2: "Java", 3: "C# book"}
    # 網頁都是用json格式呈現,不是python的字典格式,所以要轉格式
    return HttpResponse(json.dumps(my_books), content_type="application/json")
