import os
import pyodbc
import re

SERVER = '34.176.185.229'
USERNAME = 'sqlserver'
PASSWORD = 'a<lVE)5<pI5pd\d~'

SQL_FOLDER = './scripts_sql'

expected_dbs = [
    'DW_VENTAS',
    'PARK_1_JUJUY_ENTRADAS',
    'PARK_1_JUJUY_PRODUCTOS',
    'PARK_2_BUENOSAIRES_ENTRADAS',
    'PARK_2_BUENOSAIRES_PRODUCTOS',
    'PARK_3_FORMOSA_ENTRADAS',
    'PARK_3_FORMOSA_PRODUCTOS',
    'RRHH',
    'EXTERNO_ESCUELAS'
]

def execute_sql_file_on_master(script_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        statements = []
        if script_path == "./scripts_sql\INSERT_ESCUELAS.sql":
            statements = [sql_script.removesuffix("GO")]
        else:
            statements = [
                stmt.strip() for stmt in re.split(r'\bGO\b', sql_script)
                if stmt.strip()
            ]

        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};DATABASE=master;UID={USERNAME};PWD={PASSWORD};',
            autocommit=True
        )
        cursor = conn.cursor()

        for statement in statements:
            cursor.execute(statement)
            while cursor.nextset():
                pass

        conn.commit()
        print(f"Executed: {os.path.basename(script_path)}")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed executing {os.path.basename(script_path)}: {e}")

try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SERVER};DATABASE=master;UID={USERNAME};PWD={PASSWORD};'
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name FROM sys.databases
        WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')
    """)
    existing_dbs = [row[0] for row in cursor.fetchall()]

    print("Connected to SQL Server.")
    print("Existing databases:")
    for db in existing_dbs:
        print(f"  - {db}")

    print("Processing SQL files:")

    for db in expected_dbs:
        script_path = os.path.join(SQL_FOLDER, f"{db}.sql")
        if os.path.exists(script_path):
            if db in existing_dbs:
                print(f"{db} exists. Executing script.")
            else:
                print(f"{db} does not exist. Executing script.")
            execute_sql_file_on_master(script_path)
            if db == "EXTERNO_ESCUELAS":
                insert_school_path = os.path.join(SQL_FOLDER, "INSERT_ESCUELAS.sql")
                execute_sql_file_on_master(insert_school_path)
        else:
            print(f"Missing SQL script for {db}: {script_path}")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Connection or execution error: {e}")
