import pyodbc
import sys

# Database connection settings
SERVER = '34.176.185.229'
USERNAME = 'sqlserver'
PASSWORD = 'a<lVE)5<pI5pd\d~'

def get_db_connection(database):
    try:
        return pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};DATABASE={database};UID={USERNAME};PWD={PASSWORD};'
        )
    except pyodbc.Error as e:
        print(f"Error connecting to database {database}: {str(e)}")
        sys.exit(1)

def remove_dw_ventas_data():
    """Remove all data from DW_VENTAS database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection('DW_VENTAS')
        cursor = conn.cursor()
        
        print("Removing data from DW_VENTAS...")
        
        # Delete in correct order to respect foreign key constraints
        # First delete from fact table
        cursor.execute("DELETE FROM FT_Ventas")
        print("Removed data from FT_Ventas")
        
        # Then delete from dimension tables
        cursor.execute("DELETE FROM DIM_Tiempo")
        print("Removed data from DIM_Tiempo")
        
        cursor.execute("DELETE FROM DIM_Producto")
        print("Removed data from DIM_Producto")
        
        cursor.execute("DELETE FROM DIM_Empleado")
        print("Removed data from DIM_Empleado")
        
        cursor.execute("DELETE FROM DIM_Escuela")
        print("Removed data from DIM_Escuela")
        
        cursor.execute("DELETE FROM DIM_Capacitacion")
        print("Removed data from DIM_Capacitacion")
        
        cursor.execute("DELETE FROM DIM_Parque")
        print("Removed data from DIM_Parque")
        
        # Reinsert the default values for dimension tables
        print("Reinserting default values for dimension tables...")
        
        # DIM_Parque default values
        cursor.execute("""
            INSERT INTO DIM_Parque(id_parque, region, nombre) VALUES
            (1, 'NORTE', 'Parque Temático Sparkle Jujuy'),
            (2, 'CENTRO-OESTE', 'Parque Temático Sparkle Buenos Aires'),
            (3, 'NORTE', 'Parque Temático Sparkle Formosa'),
            (999, '', '')
        """)
        
        # DIM_Capacitacion default values
        cursor.execute("""
            INSERT INTO DIM_Capacitacion(id_rango_horas, min_horas, max_horas) VALUES
            (1, 0, 5),
            (2, 6, 10),
            (3, 11, 20),
            (4, 21, 50),
            (5, 51, 1000),
            (999, -1, -1)
        """)
        
        # DIM_Escuela default values
        cursor.execute("""
            INSERT INTO DIM_Escuela(id_escuela, tipo_escuela) VALUES
            (1, 'Publica'),
            (2, 'Privada'),
            (999, '')
        """)
        
        # DIM_Empleado default value
        cursor.execute("""
            INSERT INTO DIM_Empleado(nro_legajo, nombre, apellido) 
            VALUES (9999, '', '')
        """)
        
        # DIM_Producto default value
        cursor.execute("""
            INSERT INTO DIM_Producto(rubro, subrubro, descripcion) 
            VALUES ('', '', '')
        """)
        
        conn.commit()
        print("Successfully removed all data from DW_VENTAS and restored default values")
    except Exception as e:
        print(f"Error removing data from DW_VENTAS: {str(e)}")
        if conn:
            conn.rollback()
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    remove_dw_ventas_data() 