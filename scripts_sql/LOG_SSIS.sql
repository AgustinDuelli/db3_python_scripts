USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'LOG_SSIS')
    BEGIN
        CREATE DATABASE LOG_SSIS;
    END
GO

USE LOG_SSIS;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Log_DIM_Producto' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Log_DIM_Producto] (
                            [id_log] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                            [ErrorCode] int NOT NULL,
                            [ErrorColumn] int NOT NULL,
                            [producto] varchar(100),
                            [subrubro] varchar(100),
                            [rubro] varchar(100),
                            [StepInProcess] varchar(200) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Log_DIM_Empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Log_DIM_Empleado] (
                            [id_log] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                            [ErrorCode] int NOT NULL,
                            [ErrorColumn] int NOT NULL,
                            [nombre] varchar(100),
                            [apellido] varchar(100),
                            [StepInProcess] varchar(200) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Log_FT_Ventas_Productos' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Log_FT_Ventas_Productos] (
                            [id_log] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                            [ErrorCode] int NOT NULL,
                            [ErrorColumn] int NOT NULL,
                            [StepInProcess] varchar(200) NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Log_FT_Ventas_Entradas' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Log_FT_Ventas_Entradas] (
                            [id_log] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
                            [ErrorCode] int NOT NULL,
                            [ErrorColumn] int NOT NULL,
                            [StepInProcess] varchar(200) NOT NULL
        );
    END
GO