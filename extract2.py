import os
import pandas as pd
import datetime
from sqlalchemy import create_engine
from sklearn.datasets import fetch_california_housing

BD_KEY = os.getenv("BD_KEY")

import MySQLdb

# Conectar a la base de datos
db = MySQLdb.connect(
    host="localhost",  # O "127.0.0.1" si es necesario
    user="root",
    passwd=BD_KEY,
    db="houses"
)

ahora = datetime.datetime.now()
print(f'Extrac - La fecha es: {ahora}')

cursor = db.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM raw")

# Recuperar resultados
resultados = cursor.fetchall()

# Mostrar resultados
for fila in resultados:
    print(fila)

# Cerrar conexión
db.close()
