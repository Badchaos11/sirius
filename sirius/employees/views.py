from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *


# Верхнее меню
menu = [{'title': "Добавить новых работников", 'url_name': 'add_page'},
        {'title': "Изменить данные работников", 'url_name': 'update_page'},
        {'title': "Удалить работника", 'url_name': 'delete_page'},
        {'title': "Список работников", 'url_name': 'home'}
]


# Главная страница, на которую выводятся все записи и где происходит фильтрация
def index(request):

    if request.method == "POST":  # Проверка на тип запрса
        form = FilterEmployee(request.POST)    # Получение данных из формы
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data['filial'] != "-" and data['position'] != "-":
                empl = Employee.objects.filter(filial=data['filial'], position=data['position'])  # Получение данных
                context = {  # Контекст для вывода на экран
                    'employees': empl,
                    "menu": menu,
                    'title': 'Список работников',
                    "form": form
                }
                return render(request, 'employees/index.html', context=context)  # Отображение страницы
            elif data['filial'] == "-" and data['position'] != "-":
                empl = Employee.objects.filter(position=data['position'])
                context = {
                    'employees': empl,
                    "menu": menu,
                    'title': 'Список работников',
                    "form": form
                }
                return render(request, 'employees/index.html', context=context)
            elif data['filial'] != "-" and data['position'] == "-":
                empl = Employee.objects.filter(filial=data['filial'])
                context = {
                    'employees': empl,
                    "menu": menu,
                    'title': 'Список работников',
                    "form": form
                }
                return render(request, 'employees/index.html', context=context)
            elif data['filial'] == "-" and data['position'] == "-":
                empl = Employee.objects.all()
            context = {
                'employees': empl,
                "menu": menu,
                'title': 'Список работников',
                "form": form
            }
            return render(request, 'employees/index.html', context=context)
    else:
        empl = Employee.objects.all()  # Если параметры не заданы, то выводится всё
        form = FilterEmployee()  # Получение полей для создания пустой формы
        context = {  # Создание контекста
            'employees': empl,
            "menu": menu,
            'title': 'Список работников',
            "form": form
        }

    return render(request, 'employees/index.html', context=context)  # Отрисовка страницы


def addpage(request):  # Создание новой записи
    if request.method == "POST":  # Проверка типа запроса
        form = NewEmployee(request.POST)  # Получение данных из формы
        if form.is_valid():  # Валидация формы
            print(form.cleaned_data)
            messages.success(request, "Данные нового работника успешно добавлены")
            form.save()  # Сохранение в БД
            return redirect("home")  # Перенаправление на главную страницу
    else:
        form = NewEmployee()  # Создание пустой формы
    return render(request, 'employees/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление работника'})


def updatepage(request):
    if request.method == "POST":  # Проверка типа запроса
        form = UpdateEmployee(request.POST)  # Получение данных из формы
        if form.is_valid():  # Валидация
            try:
                to_update = Employee.objects.get(id=form.cleaned_data['id'])  # Проверка на существование записи

                to_update.filial = form.cleaned_data['filial']  # Если успешно, то обновляем запись
                to_update.position = form.cleaned_data['position']  # Вписываем данные из формы
                to_update.salary = form.cleaned_data['salary']
                to_update.save()  # Сохранение результата
                return redirect("home")  # Перенаправление на главную страницу
            except:
                form = UpdateEmployee()  # Создание пустой формы при неудаче обновления, перенаправления не происходит
                return render(request, 'employees/updatepage.html',  # Отрисовка страницы
                              {'form': form, 'menu': menu, 'title': 'Изменение данных работника'})
    else:
        form = UpdateEmployee()  # Создание пустой формы
    return render(request, 'employees/updatepage.html',  # Отрисовка
                  {'form': form, 'menu': menu, 'title': 'Изменение данных работника'})


def deletepage(request):  # Удаление записи
    if request.method == "POST":  # Проверка типа запроса
        form = DeleteEmployee(request.POST)  # Получение данных из формы
        if form.is_valid():  # Валидация
            try:
                to_delete = Employee.objects.get(id=form.cleaned_data['id'])  # Получение записи из БД
                to_delete.delete()  # Удаление записи
                return redirect("home")  # Перенаправление на главную страницу
            except:
                form = DeleteEmployee()  # При неудаче удаления происходит отрисовка страницы удаления
                return render(request, 'employees/deletepage.html',
                              {'form': form, 'menu': menu, 'title': 'Удаление работника'})

    else:
        form = DeleteEmployee()  # Создание пустой формы
    return render(request, 'employees/deletepage.html',  # Отрисовка страницы
                  {'form': form, 'menu': menu, 'title': 'Удаление работника'})
