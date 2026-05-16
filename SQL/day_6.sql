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