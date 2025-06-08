import pyodbc
import random
from faker import Faker
from datetime import date, timedelta

SERVER = '34.176.185.229'
USERNAME = 'sqlserver'
PASSWORD = 'a<lVE)5<pI5pd\d~'

# Connection setup
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};DATABASE=DW_VENTAS;UID={USERNAME};PWD={PASSWORD};',
    autocommit=True
)
cursor = conn.cursor()
fake = Faker()

'''
# --- Insert DIM_Producto ---
rubros = ['Alimentos', 'Electrónica', 'Juguetería', 'Ropa', 'Libros']
subrubros = {
    'Alimentos': ['Snacks', 'Bebidas', 'Dulces'],
    'Electrónica': ['Audio', 'Video', 'Computación'],
    'Juguetería': ['Muñecos', 'Juegos de mesa', 'Puzzles'],
    'Ropa': ['Hombre', 'Mujer', 'Niños'],
    'Libros': ['Ficción', 'No ficción', 'Infantil']
}

print("Inserting DIM_Producto...")
for _ in range(10):
    rubro = random.choice(rubros)
    subrubro = random.choice(subrubros[rubro])
    descripcion = fake.word().capitalize() + " " + fake.word().capitalize()
    cursor.execute("""
        INSERT INTO DIM_Producto (rubro, subrubro, descripcion)
        VALUES (?, ?, ?)
    """, rubro, subrubro, descripcion)

# --- Insert DIM_Empleado ---
print("Inserting DIM_Empleado...")
empleados_ids = []
for legajo in range(2001, 2011):  # 10 empleados
    nombre = fake.first_name()
    apellido = fake.last_name()
    empleados_ids.append(legajo)
    cursor.execute("""
        INSERT INTO DIM_Empleado (nro_legajo, nombre, apellido)
        VALUES (?, ?, ?)
    """, legajo, nombre, apellido)
'''
# --- Insert FT_Ventas ---
print("Inserting FT_Ventas...")
# Get foreign keys
cursor.execute("SELECT id_tiempo FROM DIM_Tiempo")
tiempos = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id_producto FROM DIM_Producto")
productos = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id_parque FROM DIM_Parque")
parques = [row[0] for row in cursor.fetchall() if row[0] != 999]

cursor.execute("SELECT nro_legajo FROM DIM_Empleado")
empleados_ids = [row[0] for row in cursor.fetchall() if row[0] != 999]

rango_capacitacion = [1, 2, 3, 4, 5]
escuelas = [1, 2]

for _ in range(100):  # 100 ventas
    venta = (
        random.choice(tiempos),
        random.choice(parques),
        random.choice(productos),
        random.choice(empleados_ids),
        random.choice(rango_capacitacion),
        random.choice(escuelas),
        random.randint(1, 20),  # UnidadesProductos
        random.randint(100, 2000),  # BrutoProductos
        random.randint(1, 10),  # CantidadEntradas
        random.randint(100, 1000),  # BrutoEntradas
    )
    cursor.execute("""
        INSERT INTO FT_Ventas (
            id_tiempo, id_parque, id_producto, id_empleado,
            rango_horas_capacitacion, id_escuela,
            UnidadesProductos, BrutoProductos,
            CantidadEntradas, BrutoEntradas
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, *venta)

conn.commit()
print("Data inserted successfully.")

cursor.close()
conn.close()
