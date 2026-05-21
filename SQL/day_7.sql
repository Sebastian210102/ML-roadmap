/*
Diseño de una base de datos

¿Qué es una entidad?
° Es una representación de algo
° En base de datos una entidad es una tabla
Por ejemplo la tabla empleados 
Clientes, y dentro de esto tenemos 
Atributos que describen a la entidad 
Lo que contiene la tablas son los atributos 


Por ejemplo la tabla 

EMPLEADOS
*IDEmpleado - PK
*Nombre - Tipo
*Fecha_contratacion -tipo
*IDDepartamento _ FK

DEPARTAMENTOS 
*IDDepartamento - PK
*Nombre - Tipo


Los diagrama de entidad relación es una forma gráfica de como se relacionan las tablas una de otra


*** Claves primarias y foraneas

Primaria: Es un campo unico de cada tabla e identifica cada fila como algo exclusivo, por lo que no se puede repetir en otras 
entradas

Foranea: Es un campo en el que nos ayuda a referenciar la clase primaria de otra tabla en la tabla actual

Normalización : 

1NF (Primera forma normal)
*Cada columna debe contener valores atómicos y únicos
2NF 
* Si esta e 1NF si todos los atributos no clave depende de la clave primaria, o sea no hay dependecia parcial
3NF 
*No haya dependencia transtivas, todos dependen de la clabe primaria 

*/