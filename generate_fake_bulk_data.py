import pyodbc
import random
from datetime import datetime, timedelta
from faker import Faker
import sys
import time

# Database connection settings
SERVER = '34.176.185.229'
USERNAME = 'sqlserver'
PASSWORD = 'a<lVE)5<pI5pd\d~'

# Initialize Faker
fake = Faker('es_ES')

# Store start time
start_time = time.time()

def get_timestamp():
    """Get current timestamp and elapsed time"""
    current_time = datetime.now().strftime('%H:%M:%S')
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = elapsed % 60
    return f"[{current_time} +{minutes}m{seconds:.2f}s]"

def get_db_connection(database):
    try:
        return pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};DATABASE={database};UID={USERNAME};PWD={PASSWORD};'
        )
    except pyodbc.Error as e:
        print(f"{get_timestamp()} Error connecting to database {database}: {str(e)}")
        sys.exit(1)

def get_employees_from_rrhh():
    """Get all employees from RRHH database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection('RRHH')
        cursor = conn.cursor()
        cursor.execute("SELECT legajo, nombre, apellido, fecha_ingreso FROM Empleado")
        employees = cursor.fetchall()
        if not employees:
            print(f"{get_timestamp()} Error: No employees found in RRHH database")
            sys.exit(1)
        print(f"{get_timestamp()} Successfully retrieved {len(employees)} employees from RRHH")
        return employees
    except Exception as e:
        print(f"{get_timestamp()} Error getting employees from RRHH: {str(e)}")
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def calculate_seniority_factor(fecha_ingreso):
    """Calculate a seniority factor based on years of service"""
    today = datetime.now().date()  # Convert to date object
    years_of_service = (today - fecha_ingreso).days / 365.25
    # Cap the factor between 1.0 and 2.0
    return min(2.0, max(1.0, 1.0 + (years_of_service / 10)))

def get_schools_from_externo():
    """Get all schools from EXTERNO_ESCUELAS database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection('EXTERNO_ESCUELAS')
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, telefono, domicilio, sector, jurisdiccion FROM Escuela")
        schools = cursor.fetchall()
        if not schools:
            print(f"{get_timestamp()} Error: No schools found in EXTERNO_ESCUELAS database")
            sys.exit(1)
        print(f"{get_timestamp()} Successfully retrieved {len(schools)} schools from EXTERNO_ESCUELAS")
        return schools
    except Exception as e:
        print(f"{get_timestamp()} Error getting schools from EXTERNO_ESCUELAS: {str(e)}")
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def generate_categories_and_products():
    """Generate a consistent list of categories, subcategories and products"""
    try:
        categories = [
            ('Alimentos', [
                ('Snacks', [
                    'Papas Fritas Clásicas',
                    'Papas Fritas Onduladas',
                    'Nachos con Queso',
                    'Palitos Salados',
                    'Mix de Frutos Secos'
                ]),
                ('Bebidas', [
                    'Agua Mineral 500ml',
                    'Gaseosa Cola 500ml',
                    'Gaseosa Naranja 500ml',
                    'Jugo de Manzana 500ml',
                    'Agua Saborizada 500ml'
                ]),
                ('Golosinas', [
                    'Caramelos Surtidos',
                    'Chocolate con Leche',
                    'Chocolate Blanco',
                    'Gomitas de Frutas',
                    'Chupetines Surtidos'
                ]),
                ('Comidas Rápidas', [
                    'Hamburguesa Clásica',
                    'Hamburguesa con Queso',
                    'Pancho Completo',
                    'Pizza por Porción',
                    'Ensalada César'
                ])
            ]),
            ('Souvenirs', [
                ('Imanes', [
                    'Imán Parque Temático',
                    'Imán Atracción Principal',
                    'Imán Mascota del Parque',
                    'Imán Vista Panorámica',
                    'Imán Colección Especial'
                ]),
                ('Llaveros', [
                    'Llavero Logo del Parque',
                    'Llavero Atracción Popular',
                    'Llavero Mascota',
                    'Llavero Personalizado',
                    'Llavero Coleccionable'
                ]),
                ('Tazas', [
                    'Taza Logo del Parque',
                    'Taza Atracciones',
                    'Taza Mascota',
                    'Taza Vista Panorámica',
                    'Taza Edición Especial'
                ]),
                ('Camisetas', [
                    'Camiseta Logo del Parque',
                    'Camiseta Atracciones',
                    'Camiseta Mascota',
                    'Camiseta Vista Panorámica',
                    'Camiseta Edición Limitada'
                ])
            ]),
            ('Juguetes', [
                ('Pelotas', [
                    'Pelota de Playa',
                    'Pelota de Fútbol',
                    'Pelota de Voley',
                    'Pelota de Goma',
                    'Pelota con Logo del Parque'
                ]),
                ('Muñecos', [
                    'Muñeco Mascota del Parque',
                    'Muñeco Personaje Principal',
                    'Muñeco Colección Especial',
                    'Muñeco Interactivo',
                    'Muñeco Edición Limitada'
                ]),
                ('Juegos de Mesa', [
                    'Juego del Parque',
                    'Memotest Temático',
                    'Dominó Personalizado',
                    'Ludo del Parque',
                    'Trivia Temática'
                ]),
                ('Juguetes Educativos', [
                    'Rompecabezas del Parque',
                    'Kit de Ciencias',
                    'Juego de Memoria',
                    'Kit de Arte',
                    'Juego de Construcción'
                ])
            ]),
            ('Ropa', [
                ('Camisetas', [
                    'Camiseta Básica',
                    'Camiseta Estampada',
                    'Camiseta Manga Larga',
                    'Camiseta Personalizada',
                    'Camiseta Colección'
                ]),
                ('Gorras', [
                    'Gorra Clásica',
                    'Gorra Ajustable',
                    'Gorra con Visera',
                    'Gorra Personalizada',
                    'Gorra Edición Especial'
                ]),
                ('Bufandas', [
                    'Bufanda Logo del Parque',
                    'Bufanda Atracciones',
                    'Bufanda Mascota',
                    'Bufanda Personalizada',
                    'Bufanda Colección'
                ]),
                ('Medias', [
                    'Medias Logo del Parque',
                    'Medias Atracciones',
                    'Medias Mascota',
                    'Medias Personalizadas',
                    'Medias Colección'
                ])
            ])
        ]
        return categories
    except Exception as e:
        print(f"{get_timestamp()} Error generating categories and products: {str(e)}")
        sys.exit(1)

def calculate_seasonal_factor(date, park_number):
    """Calculate a seasonal factor based on the date and park number
    Park 1 (Jujuy) and 3 (Formosa):
    - Summer (Dec-Feb): 1.00-1.35 (high season)
    - Winter (Jun-Aug): 1.00-1.35 (high season)
    - Spring (Sep-Nov): 0.65-0.85 (low season)
    - Autumn (Mar-May): 0.65-0.85 (low season)
    
    Park 2 (Buenos Aires):
    - Summer (Dec-Feb): 1.00-1.35 (high season)
    - Spring (Sep-Nov): 1.00-1.35 (high season)
    - Autumn (Mar-May): 1.00-1.35 (high season)
    - Winter (Jun-Aug): 0.65-0.85 (low season)
    """
    month = date.month
    
    # Determine if it's a high season based on park number
    if park_number in [1, 3]:  # Jujuy and Formosa
        # High season: Summer and Winter
        if month in [12, 1, 2] or month in [6, 7, 8]:
            return random.uniform(1.00, 1.35)
        # Low season: Spring and Autumn
        else:  # 3,4,5 (Autumn) or 9,10,11 (Spring)
            return random.uniform(0.65, 0.85)
    else:  # Park 2 (Buenos Aires)
        # High season: Summer, Spring, Autumn
        if month in [12, 1, 2] or month in [9, 10, 11] or month in [3, 4, 5]:
            return random.uniform(1.00, 1.35)
        # Low season: Winter
        else:  # 6, 7, 8
            return random.uniform(0.65, 0.85)

def insert_categories_and_products(database, employees, schools, start_date, end_date):
    """Insert categories and products into a PRODUCTOS database using the same data"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection(database)
        cursor = conn.cursor()
        
        # Determine park number from database name
        park_number = int(database.split('_')[1])
        
        categories = generate_categories_and_products()
        
        # Determine which schema to use based on the database name
        is_park1 = database == 'PARK_1_JUJUY_PRODUCTOS'
        
        # Insert categories in bulk
        print(f"{get_timestamp()} Loading {database}.Categoria...")
        category_names = [cat_name for cat_name, _ in categories]
        if is_park1:
            cursor.executemany("""
                INSERT INTO Categoria (descripción)
                VALUES (?)
            """, [(name,) for name in category_names])
        else:
            cursor.executemany("""
                INSERT INTO Cat (descripcion)
                VALUES (?)
            """, [(name,) for name in category_names])
        
        # Get category IDs
        if is_park1:
            cursor.execute("SELECT id_categoria, descripción FROM Categoria ORDER BY id_categoria")
        else:
            cursor.execute("SELECT cod_cat, descripcion FROM Cat ORDER BY cod_cat")
        category_ids = {row[1]: row[0] for row in cursor.fetchall()}
        
        # Prepare subcategory data
        print(f"{get_timestamp()} Loading {database}.Subcategoria...")
        subcategory_data = []
        for cat_name, subcats in categories:
            cat_id = category_ids[cat_name]
            for subcat_name, _ in subcats:
                subcategory_data.append((cat_id, subcat_name))
        
        # Insert subcategories in bulk
        if is_park1:
            cursor.executemany("""
                INSERT INTO Subcategoria (id_categoria, descripción)
                VALUES (?, ?)
            """, subcategory_data)
        else:
            cursor.executemany("""
                INSERT INTO Subcat (cod_cat, [desc])
                VALUES (?, ?)
            """, subcategory_data)
        
        # Get subcategory IDs
        if is_park1:
            cursor.execute("SELECT id_subcategoria, descripción FROM Subcategoria ORDER BY id_subcategoria")
        else:
            cursor.execute("SELECT cod_subcat, [desc] FROM Subcat ORDER BY cod_subcat")
        subcategory_ids = {row[1]: row[0] for row in cursor.fetchall()}
        
        # Prepare product data
        print(f"{get_timestamp()} Loading {database}.Producto...")
        product_data = []
        for cat_name, subcats in categories:
            for subcat_name, products in subcats:
                subcat_id = subcategory_ids[subcat_name]
                for product_name in products:
                    price = round(random.uniform(100, 5000), 2)
                    product_data.append((subcat_id, product_name, price))
        
        # Insert products in bulk
        if is_park1:
            cursor.executemany("""
                INSERT INTO Producto (id_subcategoria, descripción, precio_actual)
                VALUES (?, ?, ?)
            """, product_data)
        else:
            cursor.executemany("""
                INSERT INTO Prod (cod_subcat, [desc], precio_actual)
                VALUES (?, ?, ?)
            """, product_data)
        
        # Get product IDs
        if is_park1:
            cursor.execute("SELECT id_producto, descripción FROM Producto ORDER BY id_producto")
        else:
            cursor.execute("SELECT cod_prod, [desc] FROM Prod ORDER BY cod_prod")
        product_ids = {row[1]: row[0] for row in cursor.fetchall()}
        
        # Insert employees in bulk
        print(f"{get_timestamp()} Loading {database}.Empleado...")
        employee_data = [(emp.nombre, emp.apellido) for emp in employees]
        if is_park1:
            cursor.executemany("""
                INSERT INTO Empleado (nombre, apellido)
                VALUES (?, ?)
            """, employee_data)
        else:
            cursor.executemany("""
                INSERT INTO Empleado (nombre, apellido)
                VALUES (?, ?)
            """, employee_data)
        
        # Get employee IDs
        if is_park1:
            cursor.execute("SELECT id_empleado FROM Empleado ORDER BY id_empleado")
        else:
            cursor.execute("SELECT cod_empleado FROM Empleado ORDER BY cod_empleado")
        employee_ids = {emp.legajo: row[0] for emp, row in zip(employees, cursor.fetchall())}
        
        # Insert schools in bulk
        print(f"{get_timestamp()} Loading {database}.Escuela...")
        school_data = [(school.nombre, school.domicilio) for school in schools]
        if is_park1:
            cursor.executemany("""
                INSERT INTO Escuela (nombre, domicilio)
                VALUES (?, ?)
            """, school_data)
        else:
            cursor.executemany("""
                INSERT INTO Escuela (nombre, domicilio)
                VALUES (?, ?)
            """, school_data)
        
        # Get school IDs
        if is_park1:
            cursor.execute("SELECT id_escuela FROM Escuela ORDER BY id_escuela")
        else:
            cursor.execute("SELECT cod_escuela FROM Escuela ORDER BY cod_escuela")
        school_ids = [row[0] for row in cursor.fetchall()]
        
        # Insert school phones in bulk
        print(f"{get_timestamp()} Loading {database}.Telefono_escuela...")
        school_phones = [(school_id, school.telefono) 
                        for school_id, school in zip(school_ids, schools) 
                        if school.telefono]
        if school_phones:
            if is_park1:
                cursor.executemany("""
                    INSERT INTO Telefono_escuela (id_escuela, teléfono_escuela)
                    VALUES (?, ?)
                """, school_phones)
            else:
                cursor.executemany("""
                    INSERT INTO Telefono_escuela (cod_escuela, tel_escuela)
                    VALUES (?, ?)
                """, school_phones)
        
        # Prepare sales data
        print(f"{get_timestamp()} Loading {database}.Venta...")
        venta_data = []
        item_venta_data = []
        current_date = start_date
        
        while current_date <= end_date:
            # Generate 1-5 sales per day
            daily_sales = random.randint(1, 5)
            for _ in range(daily_sales):
                emp = random.choice(employees)
                school_id = random.choice(school_ids)
                new_emp_id = employee_ids[emp.legajo]
                
                # Add to venta data
                venta_data.append((current_date, new_emp_id, school_id))
                
                # Generate 1-3 items per sale, ensuring no duplicates
                available_products = list(product_ids.keys())
                num_items = min(random.randint(1, 3), len(available_products))
                selected_products = random.sample(available_products, num_items)
                
                # Calculate seniority factor for this employee
                seniority_factor = calculate_seniority_factor(emp.fecha_ingreso)
                
                # Calculate seasonal factor for the current date
                seasonal_factor = calculate_seasonal_factor(current_date, park_number)
                
                # Add to item_venta data with seniority and seasonal-influenced values
                for product_name in selected_products:
                    # Base quantity between 1-5, influenced by seniority and season
                    base_quantity = random.randint(1, 5)
                    quantity = max(1, round(base_quantity * seniority_factor * seasonal_factor))
                    
                    # Base price between 100-5000, influenced by seniority and season
                    base_price = random.uniform(100, 5000)
                    price = round(base_price * seniority_factor * seasonal_factor, 2)
                    
                    item_venta_data.append((
                        product_ids[product_name],
                        quantity,
                        price
                    ))
            
            current_date += timedelta(days=1)
        
        # Insert Venta records in bulk
        if is_park1:
            cursor.executemany("""
                INSERT INTO Venta (fecha_venta, id_empleado, id_escuela)
                VALUES (?, ?, ?)
            """, venta_data)
        else:
            cursor.executemany("""
                INSERT INTO Venta (fecha_venta, cod_empleado, cod_escuela)
                VALUES (?, ?, ?)
            """, venta_data)
        
        # Get all generated ticket numbers
        if is_park1:
            cursor.execute("SELECT numero_ticket FROM Venta ORDER BY numero_ticket")
        else:
            cursor.execute("SELECT nro_ticket FROM Venta ORDER BY nro_ticket")
        ticket_nums = [row[0] for row in cursor.fetchall()]
        
        # Prepare final Item_venta data with ticket numbers
        final_item_venta_data = []
        current_ticket = 0
        items_per_ticket = len(item_venta_data) // len(ticket_nums)
        
        # Create a set to track used product IDs per ticket
        used_products = set()
        
        for ticket_num in ticket_nums:
            # Reset used products for each new ticket
            used_products.clear()
            
            # Get items for this ticket
            for _ in range(items_per_ticket):
                if current_ticket < len(item_venta_data):
                    prod_id, cant, precio = item_venta_data[current_ticket]
                    
                    # Skip if this product is already in this ticket
                    if prod_id in used_products:
                        current_ticket += 1
                        continue
                    
                    # Add to used products and final data
                    used_products.add(prod_id)
                    final_item_venta_data.append((ticket_num, prod_id, cant, precio))
                    current_ticket += 1
        
        # Insert Item_venta records in bulk
        if is_park1:
            cursor.executemany("""
                INSERT INTO Item_Venta (numero_ticket, id_producto, cantidad, precio)
                VALUES (?, ?, ?, ?)
            """, final_item_venta_data)
        else:
            cursor.executemany("""
                INSERT INTO Item_Venta (nro_ticket, cod_prod, cantidad, precio)
                VALUES (?, ?, ?, ?)
            """, final_item_venta_data)
        
        conn.commit()
        print(f"{get_timestamp()} Successfully inserted data in {database}")
    except Exception as e:
        print(f"{get_timestamp()} Error in insert_categories_and_products for {database}: {str(e)}")
        if conn:
            conn.rollback()
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_visits(database, schools, employees, start_date, end_date):
    """Insert visit data into an ENTRADAS database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection(database)
        cursor = conn.cursor()
        
        # Determine park number from database name
        park_number = int(database.split('_')[1])
        
        # First, insert schools and track their new IDs
        print(f"{get_timestamp()} Loading {database}.Escuela...")
        school_data = [(school.nombre, school.domicilio) for school in schools]
        cursor.executemany("""
            INSERT INTO Escuela (nombre_escuela, dirección_escuela)
            VALUES (?, ?)
        """, school_data)
        
        # Get all school IDs
        cursor.execute("SELECT código_escuela FROM Escuela ORDER BY código_escuela")
        school_ids = [row[0] for row in cursor.fetchall()]
        
        # Insert school phones in bulk
        school_phones = [(school_id, school.telefono) 
                        for school_id, school in zip(school_ids, schools) 
                        if school.telefono]
        if school_phones:
            cursor.executemany("""
                INSERT INTO Telefono_escuela (código_escuela, teléfono_escuela)
                VALUES (?, ?)
            """, school_phones)
        
        # Insert employees and track their new IDs
        print(f"{get_timestamp()} Loading {database}.Empleado...")
        employee_data = [(emp.nombre, emp.apellido) for emp in employees]
        cursor.executemany("""
            INSERT INTO Empleado (nombre, apellido)
            VALUES (?, ?)
        """, employee_data)
        
        # Get all employee IDs
        cursor.execute("SELECT código_empleado FROM Empleado ORDER BY código_empleado")
        employee_ids = {emp.legajo: row[0] for emp, row in zip(employees, cursor.fetchall())}
        
        # Insert categories and visit types
        print(f"{get_timestamp()} Loading {database}.Categoria...")
        visit_categories = [
            'Visita Guiada',
            'Taller Educativo',
            'Visita Especial',
            'Evento Escolar'
        ]
        
        # Insert categories in bulk
        cursor.executemany("""
            INSERT INTO Categoria (descripción_categoria)
            VALUES (?)
        """, [(cat,) for cat in visit_categories])
        
        # Get category IDs
        cursor.execute("SELECT código_categoria, descripción_categoria FROM Categoria ORDER BY código_categoria")
        category_ids = {row[1]: row[0] for row in cursor.fetchall()}
        
        print(f"{get_timestamp()} Loading {database}.Tipo_visita...")
        visit_types = [
            ('Visita Guiada Básica', 100, 'Visita Guiada'),
            ('Taller de Ciencias', 150, 'Taller Educativo'),
            ('Visita VIP', 200, 'Visita Especial'),
            ('Evento Anual', 180, 'Evento Escolar')
        ]
        
        # Insert visit types in bulk
        visit_type_data = [(vt_name, arancel, category_ids[cat_name]) 
                          for vt_name, arancel, cat_name in visit_types]
        cursor.executemany("""
            INSERT INTO Tipo_visita (descripción_tipo_visita, arancel_por_alumno, código_categoria)
            VALUES (?, ?, ?)
        """, visit_type_data)
        
        # Get visit type IDs
        cursor.execute("SELECT código_tipo_visita, descripción_tipo_visita FROM Tipo_visita ORDER BY código_tipo_visita")
        visit_type_ids = {row[1]: row[0] for row in cursor.fetchall()}
        
        # Generate and insert visits
        print(f"{get_timestamp()} Loading {database}.Venta and Item_venta...")
        visits_inserted = 0
        current_date = start_date
        
        # Prepare bulk data for Venta and Item_venta
        venta_data = []
        item_venta_data = []
        
        while current_date <= end_date:
            # Generate 1-5 visits per day
            daily_visits = random.randint(0, 10)
            for _ in range(daily_visits):
                # Generate a visit
                emp = random.choice(employees)
                school_id = random.choice(school_ids)
                new_emp_id = employee_ids[emp.legajo]
                
                # Calculate seniority factor for this employee
                seniority_factor = calculate_seniority_factor(emp.fecha_ingreso)
                
                # Calculate seasonal factor for the current date
                seasonal_factor = calculate_seasonal_factor(current_date, park_number)
                
                # Select a random visit type and get its arancel
                visit_type_name = random.choice(list(visit_type_ids.keys()))
                visit_type_id = visit_type_ids[visit_type_name]
                base_arancel = next(arancel for name, arancel, _ in visit_types if name == visit_type_name)
                
                # Calculate seniority and seasonal-influenced values
                base_students = random.randint(10, 50)
                students = max(10, round(base_students * seniority_factor * seasonal_factor))
                arancel = round(base_arancel * seniority_factor * seasonal_factor, 2)
                
                # Add to bulk data
                venta_data.append((current_date, new_emp_id, school_id))
                item_venta_data.append((visit_type_id, students, arancel))
            
            current_date += timedelta(days=1)
        
        # Insert Venta records in bulk
        cursor.executemany("""
            INSERT INTO Venta (fecha, código_empleado, código_escuela)
            VALUES (?, ?, ?)
        """, venta_data)
        
        # Get all generated nro_ticket values
        cursor.execute("SELECT nro_ticket FROM Venta ORDER BY nro_ticket")
        nro_tickets = [row[0] for row in cursor.fetchall()]
        
        # Prepare final Item_venta data with nro_tickets
        final_item_venta_data = [(nro_ticket, vt_id, cant, arancel) 
                                for (nro_ticket, (vt_id, cant, arancel)) 
                                in zip(nro_tickets, item_venta_data)]
        
        # Insert Item_venta records in bulk
        cursor.executemany("""
            INSERT INTO Item_venta (nro_ticket, código_tipo_visita, cantidad_alumnos_reales, arancel_por_alumno)
            VALUES (?, ?, ?, ?)
        """, final_item_venta_data)
        
        visits_inserted = len(venta_data)
        conn.commit()
        print(f"{get_timestamp()} Successfully inserted {visits_inserted} visits in {database}")
    except Exception as e:
        print(f"{get_timestamp()} Error in insert_visits for {database}: {str(e)}")
        if conn:
            conn.rollback()
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_employees_to_rrhh():
    """Insert employees into RRHH database"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection('RRHH')
        cursor = conn.cursor()
        
        print(f"{get_timestamp()} Loading RRHH.Empleado...")
        # Generate a list of employees with realistic data
        employees = [
            ('Juan', 'Pérez', 'Av. Rivadavia 1234', 150000.00, 12, '2020-01-15', 1),
            ('María', 'González', 'Calle Corrientes 567', 165000.00, 26, '2019-05-20', 1),
            ('Carlos', 'Rodríguez', 'Av. Santa Fe 789', 140000.00, 4, '2021-03-10', 2),
            ('Ana', 'Martínez', 'Calle Córdoba 321', 155000.00, 15, '2020-11-05', 2),
            ('Luis', 'Sánchez', 'Av. Callao 456', 160000.00, 31, '2018-07-15', 3),
            ('Laura', 'Díaz', 'Calle Florida 890', 145000.00, 61, '2022-01-20', 3),
            ('Pedro', 'López', 'Av. 9 de Julio 123', 170000.00, 55, '2017-09-30', 1),
            ('Sofía', 'Fernández', 'Calle Lavalle 456', 135000.00, 20, '2022-06-15', 2),
            ('Diego', 'Gómez', 'Av. Córdoba 789', 175000.00, 60, '2016-12-10', 3),
            ('Valentina', 'Torres', 'Calle Suipacha 321', 130000.00, 15, '2023-02-28', 1),
            ('Martín', 'Ramírez', 'Av. Libertador 654', 180000.00, 65, '2015-08-25', 2),
            ('Camila', 'Silva', 'Calle Reconquista 987', 125000.00, 10, '2023-07-01', 3),
            ('Javier', 'Morales', 'Av. del Libertador 147', 185000.00, 70, '2014-04-15', 1),
            ('Lucía', 'Ortiz', 'Calle Paraguay 258', 120000.00, 5, '2023-09-10', 2),
            ('Federico', 'Castro', 'Av. Alvear 369', 190000.00, 35, '2013-11-20', 3),
            ('Agustina', 'Méndez', 'Calle Esmeralda 741', 115000.00, 2, '2023-12-01', 1),
            ('Tomás', 'Ríos', 'Av. Quintana 852', 195000.00, 58, '2012-06-30', 2),
            ('Florencia', 'Acosta', 'Calle Montevideo 963', 110000.00, 0, '2024-01-15', 3),
            ('Nicolás', 'Medina', 'Av. Figueroa Alcorta 159', 200000.00, 51, '2011-03-15', 1),
            ('Julieta', 'Herrera', 'Calle Juncal 357', 105000.00, 17, '2024-02-01', 2)
        ]
        
        for nombre, apellido, direccion, sueldo, horas_capacitacion, fecha_ingreso, id_local in employees:
            cursor.execute("""
                INSERT INTO Empleado (nombre, apellido, dirección, sueldo, horas_capacitacion, fecha_ingreso, id_local)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, nombre, apellido, direccion, sueldo, horas_capacitacion, fecha_ingreso, id_local)
            
            # Get the last inserted legajo to use for phone number
            cursor.execute("SELECT @@IDENTITY")
            legajo = cursor.fetchone()[0]
            
            # Insert phone number for the employee
            phone = f"11-{random.randint(3000, 9999)}-{random.randint(1000, 9999)}"
            cursor.execute("""
                INSERT INTO Telefono_empleado (legajo, teléfono_empleado)
                VALUES (?, ?)
            """, legajo, phone)
        
        conn.commit() 
        print(f"{get_timestamp()} Successfully inserted {len(employees)} employees into RRHH")
    except Exception as e:
        print(f"{get_timestamp()} Error inserting employees into RRHH: {str(e)}")
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
        print(f"{get_timestamp()} Starting data insertion process...")
        
        # 1. Insert employees into RRHH
        print(f"{get_timestamp()} Inserting employees into RRHH...")
        insert_employees_to_rrhh()
        
        # 2. Get employees from RRHH
        print(f"{get_timestamp()} Getting employees from RRHH...")
        employees = get_employees_from_rrhh()
        
        # 3. Get schools from EXTERNO_ESCUELAS
        print(f"{get_timestamp()} Getting schools from EXTERNO_ESCUELAS...")
        schools = get_schools_from_externo()
        
        # Set date range for all databases
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2025, 6, 9)

        # 4. Insert categories and products for each PRODUCTOS database
        product_dbs = [
            'PARK_1_JUJUY_PRODUCTOS',
            'PARK_2_BUENOSAIRES_PRODUCTOS',
            'PARK_3_FORMOSA_PRODUCTOS'
        ]
        
        for db in product_dbs:
            print(f"{get_timestamp()} Inserting categories and products into {db}...")
            insert_categories_and_products(db, employees, schools, start_date, end_date)
        
        # 5. Insert data for each ENTRADAS database
        entrada_dbs = [
            'PARK_1_JUJUY_ENTRADAS',
            'PARK_2_BUENOSAIRES_ENTRADAS',
            'PARK_3_FORMOSA_ENTRADAS'
        ]
        
        for db in entrada_dbs:
            print(f"{get_timestamp()} Inserting data into {db}...")
            insert_visits(db, schools, employees, start_date, end_date)

        print(f"{get_timestamp()} Data insertion completed successfully!")
    except Exception as e:
        print(f"{get_timestamp()} Error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
