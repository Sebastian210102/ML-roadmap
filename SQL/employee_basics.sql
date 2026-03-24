CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER,
    years_experience INTEGER
);

INSERT INTO employees VALUES
(1, 'Ana', 'Engineering', 85000, 5),
(2, 'Luis', 'Marketing', 52000, 3),
(3, 'Sofia', 'Engineering', 92000, 8),
(4, 'Carlos', 'HR', 48000, 2),
(5, 'Maria', 'Engineering', 78000, 4),
(6, 'Pedro', 'Marketing', 61000, 6),
(7, 'Laura', 'HR', 51000, 7);


#Ahora resuelve estas queries **sin googlear**:

#1. Todos los empleados de Engineering
SELECT * FROM employees
WHERE department = 'Engineering';

#2. Empleados con salario entre 50,000 y 80,000
SELECT * FROM employees
WHERE salary BETWEEN 50000 AND 80000;
#3. Empleados de Engineering O Marketing con más de 4 años de experiencia
SELECT * 
FROM employees
WHERE ((department = 'Engineering') or (department = 'Marketing')) 
AND years_experience > 4;

#4. Empleados que NO son de HR, ordenados por salario de mayor a menor
SELECT * 
FROM employees
WHERE department <> 'HR'
ORDER BY salary DESC;