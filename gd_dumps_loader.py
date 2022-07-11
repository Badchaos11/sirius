import gspread as gd
import pymysql.cursors


gc = gd.service_account("sirius-355912-ca31fefaf074.json")

worksheet = gc.open("Sirius_DB_Dumps").worksheet("Dumps")

connection = pymysql.connect(
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
        result = cursor.fetchall()

worksheet.update("A2", list(result))
