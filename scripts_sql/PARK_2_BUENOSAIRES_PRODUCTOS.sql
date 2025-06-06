USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'PARK_2_BUENOSAIRES_PRODUCTOS')
    BEGIN
        CREATE DATABASE [PARK_2_BUENOSAIRES_PRODUCTOS];
    END
GO

USE [PARK_2_BUENOSAIRES_PRODUCTOS];
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Cat' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Cat] (
                               [cod_cat] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                               [descripcion] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Subcat' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Subcat] (
                                  [cod_subcat] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                  [cod_cat] INT NOT NULL,
                                  [desc] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Prod' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Prod] (
                                [cod_prod] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                [cod_subcat] INT NOT NULL,
                                [desc] VARCHAR(50) NOT NULL,
                                [precio_actual] FLOAT NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Empleado] (
                                    [cod_empleado] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                    [nombre] VARCHAR(50) NOT NULL,
                                    [apellido] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Escuela] (
                                   [cod_escuela] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                   [nombre] VARCHAR(150) NOT NULL,
                                   [domicilio] VARCHAR(100) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Venta' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Venta] (
                                 [nro_ticket] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                 [fecha_venta] DATE NOT NULL,
                                 [cod_empleado] INT NOT NULL,
                                 [cod_escuela] INT NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Item_Venta' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Item_Venta] (
                                      [nro_ticket] INT NOT NULL,
                                      [cod_prod] INT NOT NULL,
                                      [cantidad] INT NOT NULL,
                                      [precio] FLOAT NOT NULL,
                                      PRIMARY KEY ([nro_ticket], [cod_prod])
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Telefono_escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Telefono_escuela] (
                                            [cod_escuela] INT PRIMARY KEY NOT NULL,
                                            [tel_escuela] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Subcat_Cat')
    BEGIN
        ALTER TABLE [Subcat]
            ADD CONSTRAINT FK_Subcat_Cat
                FOREIGN KEY ([cod_cat]) REFERENCES [Cat] ([cod_cat]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Prod_Subcat')
    BEGIN
        ALTER TABLE [Prod]
            ADD CONSTRAINT FK_Prod_Subcat
                FOREIGN KEY ([cod_subcat]) REFERENCES [Subcat] ([cod_subcat]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Empleado')
    BEGIN
        ALTER TABLE [Venta]
            ADD CONSTRAINT FK_Venta_Empleado
                FOREIGN KEY ([cod_empleado]) REFERENCES [Empleado] ([cod_empleado]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Escuela')
    BEGIN
        ALTER TABLE [Venta]
            ADD CONSTRAINT FK_Venta_Escuela
                FOREIGN KEY ([cod_escuela]) REFERENCES [Escuela] ([cod_escuela]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_Venta')
    BEGIN
        ALTER TABLE [Item_Venta]
            ADD CONSTRAINT FK_ItemVenta_Venta
                FOREIGN KEY ([nro_ticket]) REFERENCES [Venta] ([nro_ticket]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_Prod')
    BEGIN
        ALTER TABLE [Item_Venta]
            ADD CONSTRAINT FK_ItemVenta_Prod
                FOREIGN KEY ([cod_prod]) REFERENCES [Prod] ([cod_prod]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_TelefonoEscuela_Escuela')
    BEGIN
        ALTER TABLE [Telefono_escuela]
            ADD CONSTRAINT FK_TelefonoEscuela_Escuela
                FOREIGN KEY ([cod_escuela]) REFERENCES [Escuela] ([cod_escuela]);
    END
GO
