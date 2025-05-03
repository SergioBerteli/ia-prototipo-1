import time
import mysql.connector
print("Conectando à base de dados...")
while(1):
    try:
        connection = mysql.connector.connect(
            user='root', password='root', host='basededados', port="3306", database='db')
        break
    except:
        print("Erro ao tentar conectar com a base de dados, tentando novamente em 5 segundos!")
        time.sleep(5)

print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()

print(students)