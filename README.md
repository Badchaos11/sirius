Простое веб-приложение для взаимодействия с базой данных MySQL.

Поддерживаются следующие функции:

  1) Создание новой записи
  
  2) Изменение существующей записи
  
  3) Удаление записи
  
  4) Вывод всех записей наглавной странице
  
  5) Вывод записей с фильтрацией по филиалу и должности. Чтобы применить только 1 фильтр во втором необходимо написать -
  
В качестве фреймворка используется Django, в нем создана одна ветка employees. Шаблоны html страниц находятся в папке templates.

Параметры подключения к БД необходимо изменить на свои в3 файлах: excell_loader.py, gd_dumpss_loader.py и по пути sirius/sirius/settings.py. На данный момент параметры имеют следующий вид: host - localhost, port - 3306, user - badchaos, password - pe0038900, db - sirius (в settings.py db это NAME).

Дополнительно ревлизовано 2 скрипта для выгрузки всей БД в файл excell и гугл таблицу.

Скрипт excell_loader.py получает все данные из таблицы базы данных и с помощью библиотеки pandas сохраняет в xlsx файл.

Скрипт gd_dumps_loader.py получает данные из таблицы. После по полученному сервисному аккаунту происходит запись в Google Sheets. Ссылка на таблицу: https://docs.google.com/spreadsheets/d/1dmoUSGS1SGtv9MuMH7rYLbhTU8qREpVZizo9i4OKY_c . 

Для получения доступа к просмотру таблицы необходимо запустить скрипт get_access.py. В нём поменять почту на свою в строке 30.
