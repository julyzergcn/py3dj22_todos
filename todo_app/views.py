import json

from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from . import models, forms


def get_todo_items():
    qs = models.TodoItem.objects.filter(deleted=False)
    qs = qs.order_by('-created_at')
    return [
        {
            'id': obj.id,
            'title': obj.title,
            'completed': obj.completed,
            'created_at': obj.created_at.date(),
        }
        for obj in qs
    ]


def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        _action = request.GET.get('_action')
        if _action in ('add_todo', 'edit_todo'):
            form = forms.TodoItemForm(data)
            if form.is_valid():
                form.save()
            # else:
            #     print('---', form.errors)
        elif _action == 'remove_todos':
            models.TodoItem.objects.filter(
                id__in=[item['id'] for item in data]).update(deleted=True)

        return JsonResponse({'todos': get_todo_items()})

    context = {
        'todo_items': json.dumps(get_todo_items(), cls=DjangoJSONEncoder),
    }

    return render(request, 'todo_home.html', context)
