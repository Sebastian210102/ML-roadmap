/*
CTE Son consultas temporales que se usan dentro de una consulta de SQL Hacen que sea mas legibles y ordenadas
Ayuda a separar las consultas en ciertos bloques, más facil de mantener
*/

WITH ListaEpisodios AS (
    SELECT serie_id, episodio_id FROM episodios
),

ListaSeries AS (
    SELECT serie_id, descripcion FROM series
)

SELECT * FROM ListaEpisodios
LEFT JOIN ListaSeries 
ON ListaEpisodios.serie_id = ListaSeries.serie_id

# Ejercicio 

WITH TituloSerie AS (
    SELECT titulo AS 'Título de la Serie', serie_id FROM Series
),

FechaSerie AS (
    SELECT MIN(fecha_estreno) AS 'Fecha del Primer Episodio', serie_id FROM Episodios
    GROUP BY serie_id
)


SELECT t.'Título de la Serie', f.'Fecha del Primer Episodio'  FROM TituloSerie t 
INNER join FechaSerie f 
ON t.serie_id = f.serie_id
ORDER BY f.'Fecha del Primer Episodio' ASC

#Ejercicio 2

WITH lanzamientos AS (
    SELECT año_lanzamiento, COUNT(año_lanzamiento) AS total_series FROM Series
    WHERE genero = 'Ciencia ficción'
    GROUP BY año_lanzamiento
)

SELECT * FROM lanzamientos


/*
Funciones de ventana: 

Realiza cálculosa través de un conjunto de filas de la tabla que están relacionadas 
con la fila actual
*/

WITH OrdenSeries AS(
SELECT titulo, año_lanzamiento
ROW_NUMBER() OVER (ORDER BY año_lanzamiento DESC) AS ordern_lanzamiento
FROM Series)

SELECT * FROM OrdenSeries
WHERE ordern_lanzamiento IN (1,2,3)

# Esto basicamente es asignar un numero el orden es basicamente lo que ponemos en el OVER

/*
Partition BY

Nos permite dividir el conjunto de resultados de una consulta en particiones
A las que luego se puede aplicar una funcion
*/

SELECT
    titulo,
    genero,
    año_lanzamiento
    ROW_NUMBER() OVER (PARTITION BY genero ORDER BY año_lanzamiento DESC) AS ranking_por_genero
FROM Series




/*
RANK: 
Como manejar el empaque, si dos o mas filas tienen el mismo valor les da el mismo rango 
*/

SELECT
    titulo,
    rating_imdb,
    RANK() OVER (ORDER BY rating_imdb DESC) AS ranking_por_genero
FROM Series

/*
DENSE_RANK: 
Necesitamos una secuencia continua de rangos, asigna rangos a las filas en una partición 
de acuerdo a un tratamiento, los rangos van a ser continuos aquí. 
*/

SELECT
    titulo,
    rating_imdb,
    DENSE_RANK() OVER (ORDER BY rating_imdb DESC) AS ranking_por_genero
FROM Episodios


/*REGEX: Son una secuencia de caracteres que gorman un patron para encontrar determinada secuencia de caracteres */

SELECT titulo, descripcion
FROM Series
WHERE descripcion REGEXP '(?i)más'

/*
PROYECTO DEL DÍA
*/

WITH EpisodiosRecientes AS(
    SELECT
        serie_id,
        COUNT(episodio_id) AS num_episodios
    FROM Episodios
    GROUP BY serie_id
),

Calificaciones AS (
    SELECT 
        serie_id, 
        AVG(rating_imdb) AS promedio_imdb
    FROM Episodios
    GROUP BY serie_id
)

SELECT s.titulo.
    er.numm_episodios,
    c.promedio_imdb
FROM Series s
JOIN EpisodiosRecientes er ON s.serie_id = er.serie_id
JOIN Calificaciones c ON s.serie_id = c.serie_id
ORDER BY c.promedio_imdb DESC, er.num_episodios DES;