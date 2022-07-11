import gspread as gd
import pymysql.cursors


def fill_gspread():
    gc = gd.service_account("sirius-355912-ca31fefaf074.json")  # Подключение сервисного аккаунта

    worksheet = gc.open("Sirius_DB_Dumps").worksheet("Dumps")  # Открытие таблицы и листа

    connection = pymysql.connect(  # Создание соединенияс БД
        host="localhost",
        port=3306,
        user="badchaos",
        password="pe0038900",
        db="sirius",
        cursorclass=pymysql.cursors.Cursor
    )

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `employees_employee`"
            cursor.execute(sql)
            result = cursor.fetchall()  # Получение всех данных из БД

    worksheet.update("A2", list(result))  # Сохранение результатов в Google Sheets
    print("Обновление документа завершено")
