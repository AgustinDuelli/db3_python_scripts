import requests

jurisdicciones = ["Jujuy", "Buenos Aires", "Formosa"]

# Prepare SQL insert statements
sql_lines = []

for jurisdiccion in jurisdicciones:
    
    api_url = f"https://data.educacion.gob.ar/buscar-escuelas?draw=20&start=0&length=20&jurisdiccion={jurisdiccion}&departamento=&localidad=&sector=0&ambito=0&nombre=&domicilio="

    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        exit()

    data = response.json()
    schools = data.get('data', [])

    for school in schools:
        nombre = (school.get('nombre') or '').strip().replace("'", "''")
        telefono = (school.get('telefono') or '').strip().replace("'", "''")
        domicilio = (school.get('domicilio') or '').strip().replace("'", "''")
        sector = (school.get('sector') or '').strip().replace("'", "''")
        juris_school = (school.get('jurisdiccion') or '').strip().replace("'", "''")

        if sector not in ['Privado', 'Estatal']:
            sector = 'Estatal'

        if nombre:
            line = (
                f"INSERT INTO Escuelas (nombre, telefono, domicilio, sector, jurisdiccion) "
                f"VALUES ('{nombre}', '{telefono}', '{domicilio}', '{sector}', '{juris_school}');"
            )
            sql_lines.append(line)

# Write to .sql file
with open('insert_escuelas.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_lines))

print("SQL script 'insert_escuelas.sql' generated successfully.")
