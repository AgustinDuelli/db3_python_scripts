USE master;
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'RRHH')
    BEGIN
        CREATE DATABASE [RRHH];
    END
GO

USE [RRHH];
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Empleado] (
                                    [legajo] int PRIMARY KEY NOT NULL IDENTITY(1001, 1),
                                    [nombre] varchar(50) NOT NULL,
                                    [apellido] varchar(50) NOT NULL,
                                    [dirección] varchar(100),
                                    [sueldo] float NOT NULL,
                                    [horas_capacitacion] int NOT NULL,
                                    [fecha_ingreso] date NOT NULL,
                                    [id_local] int NOT NULL
        );
    END
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Telefono_empleado' AND xtype = 'U')
    BEGIN
        CREATE TABLE [Telefono_empleado] (
                                             [legajo] int PRIMARY KEY NOT NULL,
                                             [teléfono_empleado] varchar(50)
        );
    END
GO

IF NOT EXISTS (
    SELECT * FROM sys.foreign_keys WHERE name = 'FK_Telefono_empleado_Empleado'
)
    BEGIN
        ALTER TABLE [Telefono_empleado]
            ADD CONSTRAINT FK_Telefono_empleado_Empleado
            FOREIGN KEY ([legajo]) REFERENCES [Empleado] ([legajo]);
    END
GO