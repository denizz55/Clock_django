from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "place", "price", "square"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Название'
            }),
            "price": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Цена'
            }),
            "place": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Количество'
            }),
            "square": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Адрес заказа'
            }),
        }
