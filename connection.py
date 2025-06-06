import pyodbc

# Server credentials
SERVER = 'DESKTOP-EGJAB17\MSSQLLOCAL'            # Adjust to your instance

# List of expected database names
expected_dbs = ['DW_VENTAS', 
                'PARK_1_JUJUY_ENTRADAS',
                'PARK_1_JUJUY_PRODUCTOS', 
                'PARK_2_BUENOSAIRES_ENTRADAS',
                'PARK_2_BUENOSAIRES_PRODUCTOS',
                'PARK_3_FORMOSA_ENTRADAS',
                'PARK_3_FORMOSA_PRODUCTOS',
                'RRHH', 
                ]  # Replace with your DBs


try:
    # Connect using Windows Authentication
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE=master;Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    # Query user databases
    cursor.execute("""
        SELECT name FROM sys.databases
        WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')
    """)
    existing_dbs = [row[0] for row in cursor.fetchall()]

    print("(OK) Connected to SQL Server with Windows Authentication.")
    print("Existing databases:")
    for db in existing_dbs:
        print(f"  - {db}")

    # Check expected DBs
    print("\n Verifying expected databases:")
    for db in expected_dbs:
        if db in existing_dbs:
            print(f"[OK] {db} exists.")
        else:
            print(f"[MISSING] {db} is missing!")

    cursor.close()
    conn.close()

except Exception as e:
    print("Failed to connect or fetch databases:", e)
