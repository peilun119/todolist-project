from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm


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
    # .order_by("-created") 代表降序排序
    todos = Todo.objects.all().order_by("-created")
    return render(request, "todo/todolist.html", {"todos": todos})


# 1.新增todo.html
# 2. 將todo傳出到{{todo}}
# 3. 修改成ModelForm
def view_todo(request, id):
    message = ""
    # 檢視目前 3
    try:
        # 從Todo模型取得id物件
        todo = Todo.objects.get(id=id)
        form = TodoForm(instance=todo)  # 3
        # context = {"id": todo.id, "title": todo.title}
        # return HttpResponse(
        #     json.dumps(context, ensure_ascii=False), content_type="application/json"
        # )
    except Exception as e:
        print(e)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)  # 3
        form.save()
        message = "更新資料成功!"
        return redirect("todolist")  # 成功後導回首頁

    return render(
        request, "todo/view-todo.html", {"todo": todo, "form": form, "message": message}
    )


# 前端建立代辦事項
def create_todo(request):
    message = ""
    form = TodoForm()
    # GET -> 進入網頁的當下就是GET

    # POST -> 按了提交的button會變POST
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        message = "新增資料成功!"
        return redirect("todolist")  # 成功後導回首頁

    return render(request, "todo/create-todo.html", {"message": message, "form": form})
