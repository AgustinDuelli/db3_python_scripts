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

def remove_data_from_database(database):
    """Remove all inserted data from a database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection(database)
        cursor = conn.cursor()
        
        # Determine which schema to use based on the database name
        is_park1 = database == 'PARK_1_JUJUY_PRODUCTOS'
        
        if database == 'RRHH':
            # Delete all employees from RRHH
            cursor.execute("DELETE FROM Telefono_empleado")
            cursor.execute("DELETE FROM Empleado")
            print(f"Successfully removed all employees from {database}")
        elif '_PRODUCTOS' in database:
            if is_park1:
                # Delete in correct order for PARK_1 schema
                cursor.execute("DELETE FROM Item_Venta")
                cursor.execute("DELETE FROM Venta")
                cursor.execute("DELETE FROM Producto")
                cursor.execute("DELETE FROM Subcategoria")
                cursor.execute("DELETE FROM Categoria")
                cursor.execute("DELETE FROM Telefono_escuela")
                cursor.execute("DELETE FROM Escuela")
                cursor.execute("DELETE FROM Empleado")
            else:
                # Delete in correct order for PARK_2 and PARK_3 schema
                cursor.execute("DELETE FROM Item_Venta")
                cursor.execute("DELETE FROM Venta")
                cursor.execute("DELETE FROM Prod")
                cursor.execute("DELETE FROM Subcat")
                cursor.execute("DELETE FROM Cat")
                cursor.execute("DELETE FROM Telefono_escuela")
                cursor.execute("DELETE FROM Escuela")
                cursor.execute("DELETE FROM Empleado")
            print(f"Successfully removed all data from {database}")
        elif '_ENTRADAS' in database:
            # Delete in correct order for ENTRADAS databases
            cursor.execute("DELETE FROM Venta")
            cursor.execute("DELETE FROM Item_venta")
            cursor.execute("DELETE FROM Tipo_visita")
            cursor.execute("DELETE FROM Categoria")
            cursor.execute("DELETE FROM Telefono_escuela")
            cursor.execute("DELETE FROM Escuela")
            cursor.execute("DELETE FROM Empleado")
            print(f"Successfully removed all data from {database}")
        
        conn.commit()
    except Exception as e:
        print(f"Error removing data from {database}: {str(e)}")
        if conn:
            conn.rollback()
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def main():
    try:
        # List of databases to clean
        databases = [
            'RRHH',  # Process RRHH first since other databases depend on it
            'PARK_1_JUJUY_PRODUCTOS',
            'PARK_1_JUJUY_ENTRADAS',
            'PARK_2_BUENOSAIRES_PRODUCTOS',
            'PARK_2_BUENOSAIRES_ENTRADAS',
            'PARK_3_FORMOSA_PRODUCTOS',
            'PARK_3_FORMOSA_ENTRADAS'
        ]
        
        for db in databases:
            print(f"Removing data from {db}...")
            remove_data_from_database(db)
        
        print("Data removal completed successfully!")
    except Exception as e:
        print(f"Error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 