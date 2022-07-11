import pandas as pd
from datetime import datetime
import pymysql.cursors


def get_excell():
    connection = pymysql.connect(  # Соединение с БД
        host="localhost",
        port=3306,
        user="badchaos",
        password="pe0038900",
        db="sirius"
    )

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `employees_employee`"
            cursor.execute(sql)
            result = cursor.fetchall()  # Получение всех данных из таблицы

    df = pd.DataFrame(result,  # Формирование датафрейма
                      columns=["ID", "Филиал", "ФИО", "Должность", "Дата рождения",
                               "Дата приема на работу", "Зарплата"])
    df.to_excel(f"Dump-{datetime.strftime(datetime.today().date(), '%Y%m%d')}.xlsx",
                index=False)  # Сохраниение в excell
    print("Документ создан")


get_excell()
