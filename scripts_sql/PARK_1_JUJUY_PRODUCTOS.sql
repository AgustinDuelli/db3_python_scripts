USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'PARK_1_JUJUY_PRODUCTOS')
    BEGIN
        CREATE DATABASE [PARK_1_JUJUY_PRODUCTOS];
    END
GO

USE [PARK_1_JUJUY_PRODUCTOS];
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Categoria' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Categoria] (
                                     [id_categoria] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                     [descripción] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Subcategoria' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Subcategoria] (
                                        [id_subcategoria] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                        [id_categoria] INT NOT NULL,
                                        [descripción] VARCHAR(50)
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Producto' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Producto] (
                                    [id_producto] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                    [id_subcategoria] INT NOT NULL,
                                    [descripción] VARCHAR(50) NOT NULL,
                                    [precio_actual] FLOAT NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Venta' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Venta] (
                                 [numero_ticket] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                 [fecha_venta] DATE NOT NULL,
                                 [id_empleado] INT NOT NULL,
                                 [id_escuela] INT NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Item_Venta' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Item_Venta] (
                                      [numero_ticket] INT NOT NULL,
                                      [id_producto] INT NOT NULL,
                                      [cantidad] INT NOT NULL,
                                      [precio] FLOAT NOT NULL,
                                      PRIMARY KEY ([numero_ticket], [id_producto])
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Empleado] (
                                    [id_empleado] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                    [nombre] VARCHAR(50) NOT NULL,
                                    [apellido] VARCHAR(50) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Escuela] (
                                   [id_escuela] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
                                   [nombre] VARCHAR(150) NOT NULL,
                                   [domicilio] VARCHAR(100) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Telefono_escuela' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Telefono_escuela] (
                                            [id_escuela] INT PRIMARY KEY NOT NULL,
                                            [teléfono_escuela] VARCHAR(50)
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Subcategoria_Categoria')
    BEGIN
        ALTER TABLE [Subcategoria]
            ADD CONSTRAINT FK_Subcategoria_Categoria
                FOREIGN KEY ([id_categoria]) REFERENCES [Categoria] ([id_categoria]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Producto_Subcategoria')
    BEGIN
        ALTER TABLE [Producto]
            ADD CONSTRAINT FK_Producto_Subcategoria
                FOREIGN KEY ([id_subcategoria]) REFERENCES [Subcategoria] ([id_subcategoria]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Empleado')
    BEGIN
        ALTER TABLE [Venta]
            ADD CONSTRAINT FK_Venta_Empleado
                FOREIGN KEY ([id_empleado]) REFERENCES [Empleado] ([id_empleado]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Escuela')
    BEGIN
        ALTER TABLE [Venta]
            ADD CONSTRAINT FK_Venta_Escuela
                FOREIGN KEY ([id_escuela]) REFERENCES [Escuela] ([id_escuela]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_Venta')
    BEGIN
        ALTER TABLE [Item_Venta]
            ADD CONSTRAINT FK_ItemVenta_Venta
                FOREIGN KEY ([numero_ticket]) REFERENCES [Venta] ([numero_ticket]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_Producto')
    BEGIN
        ALTER TABLE [Item_Venta]
            ADD CONSTRAINT FK_ItemVenta_Producto
                FOREIGN KEY ([id_producto]) REFERENCES [Producto] ([id_producto]);
    END
GO

IF NOT EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_TelefonoEscuela_Escuela')
    BEGIN
        ALTER TABLE [Telefono_escuela]
            ADD CONSTRAINT FK_TelefonoEscuela_Escuela
                FOREIGN KEY ([id_escuela]) REFERENCES [Escuela] ([id_escuela]);
    END
GO
