USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'DW_VENTAS')
    BEGIN
        CREATE DATABASE DW_VENTAS;
    END
GO

USE DW_VENTAS;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Capacitacion' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Capacitacion] (
                                            [id_rango_horas] int PRIMARY KEY NOT NULL,
                                            [min_horas] int NOT NULL,
                                            [max_horas] int NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Escuela] (
                                       [id_escuela] int PRIMARY KEY NOT NULL,
                                       [tipo_escuela] varchar(10)
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Tiempo' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Tiempo] (
                                      [id_tiempo] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                      [año] int NOT NULL,
                                      [trimestre] int NOT NULL,
                                      [mes] int NOT NULL,
                                      [semana] int NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Producto' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Producto] (
                                        [id_producto] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                        [rubro] varchar(40) NOT NULL,
                                        [subrubro] varchar(40) NOT NULL,
                                        [descripcion] varchar(40) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Parque' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Parque] (
                                      [id_parque] int PRIMARY KEY NOT NULL,
                                      [region] varchar(40) NOT NULL,
                                      [nombre] varchar(40) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'DIM_Empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [DIM_Empleado] (
                                        [nro_legajo] int PRIMARY KEY NOT NULL,
                                        [nombre] varchar(50) NOT NULL,
                                        [apellido] varchar(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'FT_Ventas' AND xtype = 'U')
    BEGIN
        CREATE TABLE [FT_Ventas] (
                                     [id_tiempo] int,
                                     [id_parque] int,
                                     [id_producto] int,
                                     [id_empleado] int,
                                     [rango_horas_capacitacion] int,
                                     [id_escuela] int,
                                     [UnidadesProductos] int,
                                     [BrutoProductos] int,
                                     [CantidadEntradas] int,
                                     [BrutoEntradas] int,
                                     PRIMARY KEY ([id_tiempo], [id_parque], [id_producto], [id_empleado], [rango_horas_capacitacion], [id_escuela])
        );
    END
GO



IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Tiempo')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Tiempo FOREIGN KEY ([id_tiempo]) REFERENCES [DIM_Tiempo] ([id_tiempo]);
    END

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Parque')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Parque FOREIGN KEY ([id_parque]) REFERENCES [DIM_Parque] ([id_parque]);
    END

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Producto')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Producto FOREIGN KEY ([id_producto]) REFERENCES [DIM_Producto] ([id_producto]);
    END

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Empleado')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Empleado FOREIGN KEY ([id_empleado]) REFERENCES [DIM_Empleado] ([nro_legajo]);
    END

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Capacitacion')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Capacitacion FOREIGN KEY ([rango_horas_capacitacion]) REFERENCES [DIM_Capacitacion] ([id_rango_horas]);
    END

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_FT_Escuela')
    BEGIN
        ALTER TABLE [FT_Ventas] ADD CONSTRAINT FK_FT_Escuela FOREIGN KEY ([id_escuela]) REFERENCES [DIM_Escuela] ([id_escuela]);
    END
GO

IF NOT EXISTS (SELECT * FROM DIM_Parque)
    BEGIN
        INSERT INTO DIM_Parque(id_parque, region, nombre) VALUES
                                                              (1, 'NORTE', 'Parque Temático Sparkle Jujuy'),
                                                              (2, 'CENTRO-OESTE', 'Parque Temático Sparkle Buenos Aires'),
                                                              (3, 'NORTE', 'Parque Temático Sparkle Formosa'),
                                                              (999, '', '');
    END
GO

IF NOT EXISTS (SELECT * FROM DIM_Capacitacion)
    BEGIN
        INSERT INTO DIM_Capacitacion(id_rango_horas,min_horas, max_horas) VALUES
                                                               (1,0, 5),
                                                               (2,6, 10),
                                                               (3,11, 20),
                                                               (4,21, 50),
                                                               (5,51, 1000),
                                                               (999,-1, -1);
    END
GO

IF NOT EXISTS (SELECT * FROM DIM_Escuela)
    BEGIN
        INSERT INTO DIM_Escuela(id_escuela, tipo_escuela) VALUES
                                                              (1, 'Publica'),
                                                              (2, 'Privada'),
                                                              (999, '');
    END
GO