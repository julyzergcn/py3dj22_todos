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
        ids = []
        item_objs = []
        for item in data:
            if item['id'] is None:
                item_objs.append(
                    models.TodoItem(title=item['title'], completed=item['completed'])
                )
                continue
            ids.append(item['id'])
            models.TodoItem.objects.filter(id=item['id'])\
                .update(title=item['title'], completed=item['completed'])

        models.TodoItem.objects.filter(deleted=False)\
            .exclude(id__in=ids).update(deleted=True)
        models.TodoItem.objects.bulk_create(item_objs)

        return JsonResponse({'todo_items': get_todo_items()})

    context = {
        'todo_items': json.dumps(get_todo_items()),
    }

    return render(request, 'todo_home.html', context)
