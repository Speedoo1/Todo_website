from django.forms import forms

from index.models import Todo_App
from django.forms import forms, ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo_App
        fields = ['title']
