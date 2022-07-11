from django import forms
from .models import *


# Создание форм для взаимодействия с веб-формами
class NewEmployee(forms.ModelForm):  # Создание новой записи
    class Meta:
        model = Employee
        fields = ["filial", "fio", "position", "birth", "comedate", "salary"]


class FilterEmployee(forms.ModelForm):  # Параметры фильтрации для вывода данных
    class Meta:
        model = Employee
        fields = ["filial", "position"]


class UpdateEmployee(forms.Form):  # Форма обновления данных, изменить можно филиал, должность и зарплату
    id = forms.IntegerField()
    filial = forms.CharField()
    position = forms.CharField()
    salary = forms.FloatField()


class DeleteEmployee(forms.Form):  # Форма удаления
    id = forms.IntegerField()
