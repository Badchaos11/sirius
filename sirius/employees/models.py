from django.db import models


class Employee(models.Model):
    filial = models.CharField(max_length=100, verbose_name="Филиал")
    fio = models.CharField(max_length=150, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    birth = models.CharField(max_length=20, verbose_name="Дата рождения")
    comedate = models.CharField(max_length=20, verbose_name="Дата приема на работу")
    salary = models.FloatField(max_length=100, verbose_name="Зарплата")
