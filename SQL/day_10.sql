/*Automatización de SQL*/

/*Vistas
Simplifican la manera en la que interactuamos con los daots y los mantiene seguros

Una vista es una tabala virtual cuyo contenido esta definido por una consulta
Al igual que una tabla, una vista consta de un conjunto de columnas y filas de datos con un nombre


Se acutualiza automáticamento

Beneficios:

Simplifican las consultas complejas
Mejoran la seguridad de los datos 
Ayudan en la consistencia de la base de datos


*/


CREATE VIEW VistaEmpleadosTecnología AS
SELECT nombre, apellido, email
FROM Empleados 
WHERE depto_id = 1;

SELECT * FROM VistaEmpleadosTecnología

#Si algo cambia de la tabla empleados tambien va a cambiar la vista 

/*
Vista materializadas 

Almacenan lo consultado localmente

*/

CREATE MATERIALIZZE VIEW VistaEmpleadosProyectos AS
SELECT Empleados.nombre, Proyectos.nombre AS Proyecto
....


/*
Triggers
Son acciones automatizadas que se ejecutan luego de que ocurra un evento específico
*/

DELIMITER $$
CREATE TRIGGER RegistrarNuevoEmpleado
AFTER INSERT ON Empleados
FOR EACH ROW
BEGIN 
    INSERT INTO LogEmpleados(empleado_id, fecha_registro) VALUES(NEW.empleado_id, NOW());
END$$

DELIMITER ; 

/*
Proyecto del día

CREAR UNA VISTA VistaEmpleadosProyectos
Nombre, apeelido del empleado con el proyecto al que esta asignado
Tablas, Empleados, Asignaciones de prpyectos y proyectos
*/

CREATE VIEW VistaEmpleadosProyectos AS
SELECT  e.nombre, e.apellido, p.nombre
FROM Empleados e
JOIN AsignacionesDeProyectos a
ON e.empleado_id = a.empleado_id
JOIN Proyectos p
ON a.proyecto_id = p.proyecto