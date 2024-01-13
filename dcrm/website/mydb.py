import mysql.connector

try:
    # Conectar a MySQL Server
    dataBase = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    # Crear un cursor
    cursorObject = dataBase.cursor()

    # Crear la base de datos
    cursorObject.execute("CREATE DATABASE comferre")

    print("pass ok")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    # Cerrar la conexión
    if 'dataBase' in locals():
        dataBase.close()
