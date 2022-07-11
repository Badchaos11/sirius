from django import forms
from .models import *


class NewEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["filial", "fio", "position", "birth", "comedate", "salary"]


class FilterEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["filial", "position"]


class UpdateEmployee(forms.Form):
    id = forms.IntegerField()
    filial = forms.CharField()
    position = forms.CharField()
    salary = forms.FloatField()


class DeleteEmployee(forms.Form):
    id = forms.IntegerField()
