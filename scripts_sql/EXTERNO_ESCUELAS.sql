USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'EXTERNO_ESCUELAS')
    BEGIN
        CREATE DATABASE EXTERNO_ESCUELAS;
    END
GO

USE EXTERNO_ESCUELAS;
GO

GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Escuela] (
                                   nombre VARCHAR(150) PRIMARY KEY NOT NULL,
                                   telefono VARCHAR(50) NOT NULL,
                                   domicilio VARCHAR(100) NOT NULL,
                                   sector VARCHAR(10) NOT NULL,
                                   jurisdiccion VARCHAR(20) NOT NULL
        )
    END
GO


IF NOT EXISTS (SELECT * FROM Escuela)
    BEGIN  
        INSERT INTO Escuela (nombre, telefono, domicilio, sector, jurisdiccion) VALUES 
            ('ESCUELA N 157 DR RICARDO ROJAS', '000000', 'CONSTITUCION 391 CUYAYA INTITUCION EDUCATIVA', 'Estatal', 'Jujuy'),
            ('ESCUELA N 396 DR ANTONIO ROCHA SOLÓRZANO', '4235115', 'OLAVARRIA 501 CUYAYA', 'Estatal', 'Jujuy'),
            ('ESCUELA N 136 GRAL LAMADRID', '4223917', 'ESCOLASTICO ZEGADA 1316 CUYAYA', 'Estatal', 'Jujuy'),
            ('ESCUELA N 85 23 DE AGOSTO', '4223386', 'CONSTITUCION 391 CUYAYA', 'Estatal', 'Jujuy'),
            ('COLEGIO PRIVADO PABLO PIZZURNO -NIVEL SECUNDARIO-', '4226260 / 4234036', 'RIOJA 1970 CUYAYA', 'Privado', 'Jujuy'),
            ('ESCUELA ESPECIAL N 7 INSTITUTO HELLEN KELLER', '4226500', 'MAGALLANES 201 CORONEL ARIAS hellenkeller@hotmail.com.ar', 'Estatal', 'Jujuy'),
            ('ESCUELA DE GESTIÓN PRIVADA ARCO IRIS', '4223242', 'BALCARCE 523 CENTRO', 'Privado', 'Jujuy'),
            ('CENTRO EDUCATIVO NIVEL SECUNDARIO N 310', '155820223', 'ESCOLASTICO ZEGADA 1316 CUYAYA', 'Estatal', 'Jujuy'),
            ('COLEGIO SANTA BARBARA', '4223009', 'SAN MARTIN 1051 CENTRO', 'Privado', 'Jujuy'),
            ('COLEGIO PRIVADO JEAN PIAGET', '4242341 (SECUNDARIO) - 4243121(PRIMARIO)', 'RAMIREZ DE VELAZCO 526 CENTRO', 'Privado', 'Jujuy'),
            ('ESCUELA N 282 TAMBOR DE TACUARI', '00000000', 'AV. MIGUEL SANCHO  ARROYO COLORADO', 'Estatal', 'Jujuy'),
            ('COLEGIO NUESTRA SEÑORA DEL HUERTO', '4236060', 'SAN MARTIN 569 CENTRO', 'Privado', 'Jujuy'),
            ('COLEGIO N 1 TEODORO SANCHEZ DE BUSTAMANTE', '4233599', 'GORRITI 343 CENTRO', 'Estatal', 'Jujuy'),
            ('ESCUELA N 173 AMÉRICA DEL SUR', '4913072', 'CENTRO', 'Estatal', 'Jujuy'),
            ('ESCUELA N 343 CABO HUMBERTO CESAR ALEMÁN HÉROE DE MALVINAS', '00000000', 'RUTA PROVINCIAL N 61 KM 7 1/2', 'Estatal', 'Jujuy'),
            ('ESCUELA N 323 MAESTROS ARGENTINOS', '4913073', 'MINETTI RUTA N 53', 'Estatal', 'Jujuy'),
            ('BACHILLERATO PROVINCIAL N 15 LEGISLATURA DE LA PROVINCIA DE JUJUY', '4235781', 'PEATONAL 25  CUYAYA', 'Estatal', 'Jujuy'),
            ('ESCUELA N 100 FRANCISCO DE ARGAÑARAZ', '4225475', 'AV. PERU 1201 MARIANO MORENO', 'Estatal', 'Jujuy'),
            ('ESCUELA ESPECIAL N 1 DR OSCAR ORIAS', '155966738', 'ESPERANZA IBANEZ DE YECORA 1201 MARIANO MORENO', 'Estatal', 'Jujuy'),
            ('CENTRO POLIVALENTE DE ARTE PROF LUIS ALBERTO MARTINEZ', '4244994', 'SANTA BARBARA 677 20 DE JUNIO', 'Estatal', 'Jujuy'),
            ('JARDÍN DE INFANTES Nº915 JAVIER VILLAFAÑE', '42-6487', 'TIRO FEDERAL 712', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº2 DOMINGO FAUSTINO SARMIENTO', '42-3361', 'COLON Y MITRE 498  epnrozazul@yahoo.com.ar', 'Estatal', 'Buenos Aires'),
            ('INSTITUTO PEDRO B. PALACIOS', '4457-0054', 'VICTOR MARTINEZ 1955', 'Privado', 'Buenos Aires'),
            ('INSTITUTO JUANA DE IBARBOUROU', '4626-1051', 'AV. ROJO 4415', 'Privado', 'Buenos Aires'),
            ('ESCUELA DE TEATRO DE MORON', '4629-3097', 'SAN MARTÍN 620', 'Estatal', 'Buenos Aires'),
            ('INSTITUTO SAN JOSÉ', '4629-0419', 'SAN MARTÍN 319', 'Privado', 'Buenos Aires'),
            ('PEDRO BONIFACIO PALACIOS ALMAFUERTE', '4628-2200', 'BLANCO ESCALADA 1846', 'Privado', 'Buenos Aires'),
            ('COLEGIO CREAR Y SER', '4627-7009', 'BAHIA BLANCA 2057', 'Privado', 'Buenos Aires'),
            ('COLEGIO SAN JOSÉ DE CALASANZ', '4459-1360', 'JUANA DE AZURDUY 201', 'Privado', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº10 SIR ALEXANDER FLEMING', '4459-6351', 'RODRIGUEZ (E/CARBAJAL Y MASSENET) 2022', 'Estatal', 'Buenos Aires'),
            ('JARDÍN DE INFANTES Nº907 MAESTRAS ARGENTINAS', '4452-4999', 'DIEGO DE CARVAJAL 892  PARQUE QUIRNO', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº22 MARTÍN FIERRO', '4665-3168', 'OCAMPO (E/ ROMA Y BELGICA) 1965  PARQUE QUIRNO', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº21 ROSARIO VERA PEÑALOZA', '4459-7363', 'ONTIVEROS 4151  EL PROGRESO', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº13 DR. TOMAS LE BRETON', '4450-5347', 'LE BRETON 4385', 'Estatal', 'Buenos Aires'),
            ('JARDÍN DE INFANTES Nº911 HEBE SAN MARTÍN DE DUPRAT', '4450-7898', 'BONORINO (E/ BELL VILLE Y THOMAS LEBRETON) 501', 'Estatal', 'Buenos Aires'),
            ('CENTRO DE ADULTOS Nº705 AVIADOR PABLO TEODORO FELS', '4450-3312', 'NIGHTINGALEN Y GUAYRA', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE EDUCACIÓN PRIMARIA Nº25 SUBTE. AVIADOR PABLO TEODORO FELS', '4450-0207', 'MAR DEL PLATA E/ ALCANTARA Y LEBHENSON 897  BARRIO MITRE', 'Estatal', 'Buenos Aires'),
            ('ESCUELA DE ADULTOS Nº701 JORGE NEWBERY', '4665-3260', 'LEVALLE 1991  WILLIAM C. MORRIS', 'Estatal', 'Buenos Aires'),
            ('CENTRO DE ADULTOS Nº707/01', '4665-3260', 'BUSTAMANTE Y GURRUCHAGA   BARRIO CARTERO', 'Estatal', 'Buenos Aires'),
            ('CENTRO DE ADULTOS Nº704/01', '4665-4144', 'DIAGONAL DE MAYO Y MUSTONI   WILLIAM C. MORRIS', 'Estatal', 'Buenos Aires'),
            ('EPEP Nº 352', '00', 'RUTA PROVINCIAL Nº39   CAMPO BANDERA', 'Estatal', 'Formosa'),
            ('EPEP Nº 352 ANEXO 1', '783493', 'RUTA PROVINCIAL Nº39   EL TREBOL', 'Estatal', 'Formosa'),
            ('EPEP Nº 352 ANEXO 2', '00', 'TRES PALMITAS', 'Estatal', 'Formosa'),
            ('EPEP Nº 220', '00', 'CAMPO GRANDE', 'Estatal', 'Formosa'),
            ('EPEP Nº 220 ANEXO 1 (EX EPEP Nº 23 ANEXO 1)', '00', 'PARAJE EL PARAISO', 'Estatal', 'Formosa'),
            ('EPET Nº 4', '4480367', 'JUAN BAUTISTA ALBERDI  LA PEÑA', 'Estatal', 'Formosa'),
            ('EPEE Nº 3', '480092', 'CRISOLOGO LARRALDE 1221 ITATI AV. CRISOLOGO LARRALDE', 'Estatal', 'Formosa'),
            ('EPEP Nº 202', '554606', 'EL BAÑADERO- RUTA PROVINCIAL N° 9', 'Estatal', 'Formosa'),
            ('EPEP Nº 229', '', 'SAN SIMON -RUTA N° 9', 'Estatal', 'Formosa'),
            ('EPEP Nº 286', '00', 'COLONIA RODA', 'Estatal', 'Formosa'),
            ('EPEP Nº 415', '', 'EL PALMAR', 'Estatal', 'Formosa'),
            ('EPEP Nº 303', '272082', 'RUTA Nº9   LA FLORESTA', 'Estatal', 'Formosa'),
            ('EPEP Nº 303 ANEXO 2 (EX EPEP Nº 370)', '00', '', 'Estatal', 'Formosa'),
            ('EPEP Nº 371 DOCENTES RURALES', '203292', 'LOTE 17-LEGUA A- CAMPO HARDY', 'Estatal', 'Formosa'),
            ('EPEP Nº 27 GRAL. RICHIERI', '', 'KILOMETRO 224 N.R.B.', 'Estatal', 'Formosa'),
            ('EPES Nº 42 ETELVINA CONCEPCIÓN BARRETO', '4000391', 'MANZANA 52  JUAN DOMINDO PERON', 'Estatal', 'Formosa'),
            ('EPEP Nº 55 DR. MARIANO BOEDO', '434243', 'A UNA CUADRA ESTACION GRAL. BELGRANO', 'Estatal', 'Formosa'),
            ('EPEP Nº 73 FRAY BME. DE LAS CASAS (EX EPEP Nº 483 ANEXO)', '', 'BARTOLOME DE LAS CASAS', 'Estatal', 'Formosa'),
            ('EPEP Nº 307 TIERRA DEL FUEGO', '03716546', 'RUTA NACIONAL Nº95   COLONIA NAPENAY', 'Estatal', 'Formosa'),
            ('NEP Y FP Nº 28 - EX EDIFICIO EPEP Nº 199', '507863', 'COLONIA ABORIGEN B.DE LAS CASAS', 'Estatal', 'Formosa');
    END
GO