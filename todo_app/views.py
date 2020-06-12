import json

from django.shortcuts import render
from django.http.response import JsonResponse

from . import models


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
            ids.append(item['id'])
        models.TodoItem.objects.filter(deleted=False).exclude(id__in=ids).update(deleted=True)
        models.TodoItem.objects.bulk_create(item_objs)
        return JsonResponse({'ret': 'ok'})

    context = {
        'todo_items': models.TodoItem.objects.filter(deleted=False),
    }
    return render(request, 'todo_home.html', context)
