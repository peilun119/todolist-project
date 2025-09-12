from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo


# Create your views here.
# 函式定要帶參數request
def index(request):

    return HttpResponse("<h1>Hello Django!</h1>")


# 練習新增一個books route
def books(resquest):
    my_books = {1: "Python", 2: "Java", 3: "C# book"}
    # 網頁都是用json格式呈現,不是python的字典格式,所以要轉格式
    return HttpResponse(json.dumps(my_books), content_type="application/json")


def todolist(request):
    # 將Todo模型所有物件回到todo
    todos = Todo.objects.all()
    return render(request, "todo/todolist.html", {"todos": todos})


# 1.新增todo.html
# 2. 將todo傳出到{{todo}}
def view_todo(request, id):
    todo = None
    try:
        # 從Todo模型取得id物件
        todo = Todo.objects.get(id=id)
        # context = {"id": todo.id, "title": todo.title}
        # return HttpResponse(
        #     json.dumps(context, ensure_ascii=False), content_type="application/json"
        # )
    except Exception as e:
        print(e)

    return render(request, "todo/view-todo.html", {"todo": todo})


# 前端建立代辦事項
def create_todo(request):
    message = ""

    # GET -> 進入網頁的當下就是GET

    # POST -> 按了提交的button會變POST
    if request.method == "POST":
        print(request.POST)  # 在網站測試輸入資料,按下提交後,會在終端機出現POST資料
        title = request.POST.get("title")
        if title == "":
            print("標題欄位不能為空!")
            message = "標題欄位不能為空"
        else:
            text = request.POST.get("text")
            important = request.POST.get("important")

            important = True if important == "on" else False  # 把on換成True

            # 建立資料
            todo = Todo.objects.create(
                title=title,  # 資料表欄位名稱=上方的 title=request.POST.get("title")
                text=text,
                important=important,
            )
            todo.save()
            message = "新增資料成功!"

    return render(request, "todo/create-todo.html", {"message": message})
