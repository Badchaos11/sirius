from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *


menu = [{'title': "Добавить новых работников", 'url_name': 'add_page'},
        {'title': "Изменить данные работников", 'url_name': 'update_page'},
        {'title': "Удалить работника", 'url_name': 'delete_page'},
        {'title': "Список работников", 'url_name': 'home'}
]


def index(request):

    if request.method == "POST":
        form = FilterEmployee(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data['filial'] != "-" and data['position'] != "-":
                empl = Employee.objects.filter(filial=data['filial'], position=data['position'])
                context = {
                    'employees': empl,
                    "menu": menu,
                    'title': 'Список работников',
                    "form": form
                }
                return render(request, 'employees/index.html', context=context)
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
        empl = Employee.objects.all()
        form = FilterEmployee()
        context = {
            'employees': empl,
            "menu": menu,
            'title': 'Список работников',
            "form": form
        }

    return render(request, 'employees/index.html', context=context)


def addpage(request):
    if request.method == "POST":
        form = NewEmployee(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            messages.success(request, "Данные нового работника успешно добавлены")
            form.save()
            return redirect("home")
    else:
        form = NewEmployee()
    return render(request, 'employees/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление работника'})


def updatepage(request):
    if request.method == "POST":
        form = UpdateEmployee(request.POST)
        if form.is_valid():
            try:
                to_update = Employee.objects.get(id=form.cleaned_data['id'])
                print(to_update)

                to_update.filial = form.cleaned_data['filial']
                to_update.position = form.cleaned_data['position']
                to_update.salary = form.cleaned_data['salary']
                to_update.save()
                return redirect("home")
            except:
                form = UpdateEmployee()
                return render(request, 'employees/updatepage.html',
                              {'form': form, 'menu': menu, 'title': 'Изменение данных работника'})
    else:
        form = UpdateEmployee()
    return render(request, 'employees/updatepage.html',
                  {'form': form, 'menu': menu, 'title': 'Изменение данных работника'})


def deletepage(request):
    if request.method == "POST":
        form = DeleteEmployee(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                to_delete = Employee.objects.get(id=form.cleaned_data['id'])
                to_delete.delete()
                return redirect("home")
            except:
                form = DeleteEmployee()
                return render(request, 'employees/deletepage.html',
                              {'form': form, 'menu': menu, 'title': 'Удаление работника'})

    else:
        form = DeleteEmployee()
    return render(request, 'employees/deletepage.html',
                  {'form': form, 'menu': menu, 'title': 'Удаление работника'})
