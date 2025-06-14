USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'PARK_1_JUJUY_ENTRADAS')
BEGIN
    CREATE DATABASE [PARK_1_JUJUY_ENTRADAS];
END
GO

USE [PARK_1_JUJUY_ENTRADAS];
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Categoria' AND xtype = 'U')
BEGIN
    CREATE TABLE [Categoria] (
        [código_categoria] INT PRIMARY KEY NOT NULL IDENTITY(1,1),
        [descripción_categoria] VARCHAR(40) NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Tipo_visita' AND xtype = 'U')
BEGIN
    CREATE TABLE [Tipo_visita] (
        [código_tipo_visita] INT PRIMARY KEY NOT NULL IDENTITY(1,1),
        [descripción_tipo_visita] VARCHAR(40) NOT NULL,
        [arancel_por_alumno] FLOAT NOT NULL,
        [código_categoria] INT NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Item_venta' AND xtype = 'U')
BEGIN
    CREATE TABLE [Item_venta] (
        [nro_ticket] INT PRIMARY KEY NOT NULL,
        [código_tipo_visita] INT NOT NULL,
        [cantidad_alumnos_reales] INT NOT NULL,
        [arancel_por_alumno] FLOAT NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Empleado' AND xtype = 'U')
BEGIN
    CREATE TABLE [Empleado] (
        [código_empleado] INT PRIMARY KEY NOT NULL IDENTITY(1,1),
        [nombre] VARCHAR(50) NOT NULL,
        [apellido] VARCHAR(50) NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Telefono_escuela' AND xtype = 'U')
BEGIN
    CREATE TABLE [Telefono_escuela] (
        [código_escuela] INT PRIMARY KEY NOT NULL,
        [teléfono_escuela] VARCHAR(50) NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Escuela' AND xtype = 'U')
BEGIN
    CREATE TABLE [Escuela] (
        [código_escuela] INT PRIMARY KEY NOT NULL IDENTITY(1,1),
        [nombre_escuela] VARCHAR(150) NOT NULL,
        [dirección_escuela] VARCHAR(100) NOT NULL
    );
END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Venta' AND xtype = 'U')
BEGIN
    CREATE TABLE [Venta] (
        [nro_ticket] INT PRIMARY KEY NOT NULL IDENTITY(1,1),
        [fecha] DATE NOT NULL,
        [código_empleado] INT NOT NULL,
        [código_escuela] INT NOT NULL
    );
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_TipoVisita_Categoria'
)
BEGIN
    ALTER TABLE [Tipo_visita] 
        ADD CONSTRAINT FK_TipoVisita_Categoria 
        FOREIGN KEY ([código_categoria]) REFERENCES [Categoria] ([código_categoria]);
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_TipoVisita'
)
BEGIN
    ALTER TABLE [Item_venta] 
        ADD CONSTRAINT FK_ItemVenta_TipoVisita 
        FOREIGN KEY ([código_tipo_visita]) REFERENCES [Tipo_visita] ([código_tipo_visita]);
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_ItemVenta_Venta'
)
BEGIN
    ALTER TABLE [Item_Venta] 
        ADD CONSTRAINT FK_ItemVenta_Venta 
        FOREIGN KEY ([nro_ticket]) REFERENCES [Venta] ([nro_ticket]);
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_TelefonoEscuela_Escuela'
)
BEGIN
    ALTER TABLE [Telefono_escuela] 
        ADD CONSTRAINT FK_TelefonoEscuela_Escuela 
        FOREIGN KEY ([código_escuela]) REFERENCES [Escuela] ([código_escuela]);
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Empleado'
)
BEGIN
    ALTER TABLE [Venta] 
        ADD CONSTRAINT FK_Venta_Empleado 
        FOREIGN KEY ([código_empleado]) REFERENCES [Empleado] ([código_empleado]);
END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_Venta_Escuela'
)
BEGIN
    ALTER TABLE [Venta] 
        ADD CONSTRAINT FK_Venta_Escuela 
        FOREIGN KEY ([código_escuela]) REFERENCES [Escuela] ([código_escuela]);
END
GO

