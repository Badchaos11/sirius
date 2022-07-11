import pandas as pd
import pymysql.cursors


connection = pymysql.connect(
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
        result = cursor.fetchall()

df = pd.DataFrame(result,
                  columns=["ID", "Филиал", "ФИО", "Должность", "Дата рождения", "Дата приема на работу", "Зарплата"])
df.to_excel("Dump.xlsx", index=False)

