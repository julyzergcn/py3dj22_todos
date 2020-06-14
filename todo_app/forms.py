from django import forms

from . import models


class ModelFormMixin:
    def __init__(self, data=None, **kwargs):
        opts = self._meta
        data = data or {}
        _id = data.pop('id', None)
        if _id is not None:
            kwargs.setdefault('instance',
                opts.model.objects.get(id=_id)
            )
        super().__init__(data=data, **kwargs)


class TodoItemForm(ModelFormMixin, forms.ModelForm):

    class Meta:
        model = models.TodoItem
        fields = ('title', 'completed')
