import json

from django.shortcuts import render
from django.http.response import JsonResponse

from . import models


def get_todo_items():
    qs = models.TodoItem.objects.filter(deleted=False)
    return [
        {
            'id': obj.id,
            'title': obj.title,
            'completed': obj.completed,
        }
        for obj in qs
    ]


def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        _action = request.GET.get('_action')
        if _action == 'add_todo':
            models.TodoItem.objects.create(
                title=data['title'], completed=data['completed'])
        elif _action == 'remove_todos':
            models.TodoItem.objects.filter(
                id__in=[item['id'] for item in data]).update(deleted=True)
        elif _action == 'edit_todo':
            models.TodoItem.objects.filter(id=data['id']).update(
                title=data['title'], completed=data['completed'])

        return JsonResponse({'todos': get_todo_items()})

    context = {
        'todo_items': json.dumps(get_todo_items()),
    }

    return render(request, 'todo_home.html', context)
