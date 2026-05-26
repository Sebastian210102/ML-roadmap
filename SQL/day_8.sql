/*
Comandos DDL (Definition)
Definen el esquema de la base de datos 

Comandos DML (Manipulation)

Se utilizan para insertar, acutalizar y eliminar datos

Comandos DQL (Query)

(SELECT) Consultar datos de la base de datos 

Comandos DCL (Control)
Concesión y renovación de permisos para los usuarios

Comandos TCL (Transactions)
Se utiliza para gestionar transacciones 

*/

# DDL

CREATE DATABASE IF NOT EXISTS EmpresaDB; 

#Crear tablas

CREATE TABLE IF NOT EXISTS Departamentos(
    depto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS Empleados(
    empleado_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email  VARCHAR(255) UNIQUE NOT NULL,
    depto_id INT, 
    FOREING KEY (depto_id) REFERENCES Departamentos(depto_id)
    ON DELETE SET NULL
);

#Modificar tabla
ALTER TABLE Departamentos ADD COLUMN email_jefe VARCHAR(155)

#eliminar tabla
DROP TABLE IF EXISTS asignacionesdeproyectos

/*Comandos DML Y CRUD*/

#insertar

INSERT INTO Departamentos (nombre, ubicacion)
VALUES('Recursos Humanos','Edificio B'),
('Marketing', 'Edificio central')

#acutalizar

UPDATE Departamentos SET ubicacion = 'Edificio R'
WHERE nombre = 'Marketing'

#Eliminar filas de tablas

DELETE FROM Departamentos 
WHERE nombre = 'MARKETING'

#Eliminar base de datos 

DELETE DATABASE basededatos

/*Creacion de usuarios y permisos

*/