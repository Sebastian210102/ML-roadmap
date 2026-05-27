/*

Procedimientos almacenados
Son bloques de codigo SQL que se guardan para poder volver a utilizarlo despues 
Te permite encapsular Código para ser consultado posteriormente

*/

DELIMITER //
CREATE PROCEDURE AgregarEmpleado( IN _nombre VARCHAR(255), IN _apellido VARCHAR(255), IN _email VARCHAR(255), IN _depto_id INT);
BEGIN
    INSERT INTO Empleados(nombre, apellido, email, depto_id) VALUES (_nombre,_apellido, _email,_deptoid)
END //

DELIMITER ;

CALL AgregarEmpleado('Elena','Ruiz','elena@gmail.coom',3);



/*
Transacciones 

Es una secuencia de operaciones realizadas en una unidad logica de trabajo
Si una transacción tiene éxito, todas las modificaciones de los datos realizadas durante la transacción
se confirman
Si una transacción encuentra errores debe cancelarse o revertirse, se borran todas las modificaciones de los datos

ACID

Atomicidad
Coherencia
Aislamiento
Durabilidad 

*/


BEGIN 
SAVEPOINT PreValidacion;
INSERT INTO asignacionesdeproyectos (proyecto_id, empleado_id, horas_asignadas) VALUES(5,1,10);
INSERT INTO asignacionesdeproyectos (proyecto_id, empleado_id, horas_asignadas) VALUES (5,2,15);

ROLLBACK TO PreValidacion;




/*Procedimiento almacenado y transacciones*/

DELIMITER //

CREATE PROCEDURE AsignarHorasAProyecto(IN proyectoId INT, IN empleadoId INT, IN horasAsignadas INT)
BEGIN
    DECLARE horasTotales INT DEFAULT 0;
    DECLARE horasMaximas INT DEFAULT 100;
    
    -- Iniciar una transacción
    START TRANSACTION;
    
    -- Establecer un punto de guardado
    SAVEPOINT PreValidacion;
    
    -- Calcular el total actual de horas asignadas al proyecto
    SELECT SUM(horas_asignadas) INTO horasTotales 
    FROM AsignacionesDeProyectos 
    WHERE proyecto_id = proyectoId;
    
    -- Asumiendo que SUM() puede devolver NULL si no hay filas, lo convertimos a 0
    SET horasTotales = IFNULL(horasTotales, 0) + horasAsignadas;
    
    -- Verificar si el total excede las horas máximas permitidas
    IF horasTotales > horasMaximas THEN
        -- Revertir a SAVEPOINT si se excede el total de horas
        ROLLBACK TO PreValidacion;
        -- Aunque el ROLLBACK TO SAVEPOINT mantiene la transacción activa, decidimos terminar la operación con un mensaje de error.
        SELECT 'Error: La asignación excede el total de horas permitidas para el proyecto.' AS mensaje;
    ELSE
        -- Insertar la nueva asignación si el total está dentro del límite
        INSERT INTO AsignacionesDeProyectos (proyecto_id, empleado_id, horas_asignadas) 
        VALUES (proyectoId, empleadoId, horasAsignadas);
        
        -- Confirmar la transacción si todas las operaciones fueron exitosas
        COMMIT;
    END IF;
END //

DELIMITER ;


# Corriendo el cosdigo

CALL AsignarHorasAProyecto(1,1,5)
CALL AsignarHorasAProyecto(1,1,10)
CALL AsignarHorasAProyecto(1,1,50) /*No tendría que poder ejecutarse*/


/*Proyecto del día de hoy
Crear un procedimiento almacenado llamado 
"Agregar departamento", debe aceptar de entrada dos parámetros
(nombre, y ubicación del departamento)
*/


DELIMITER //

CREATE PROCEDURE AgregarDepartamento(IN _nombre VARCHAR(255), IN _ubicacion VARCHAR(500))
BEGIN 
    INSERT INTO Departamentos(nombre, ubicacion) VALUES(_nombre,_ubicacion);
END //

DELIMITER ;

CALL AgregarDepartamento('Depto','Lomas de San Lorenzo')