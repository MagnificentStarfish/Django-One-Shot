from django.shortcuts import render
from todos.models import TodoList, TodoItem


def Todo_List_List(request):
    Todo_List = TodoList.objects.all()
    context = {
        "Todo_List": Todo_List,
    }
    return render(request, "Todo_list/list.html", context)
