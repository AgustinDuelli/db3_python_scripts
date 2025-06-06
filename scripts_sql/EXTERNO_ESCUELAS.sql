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
