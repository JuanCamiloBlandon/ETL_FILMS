USE film_database;

#Pregunta 1
/*
¿Cuál es la relación entre la duración de las películas, su clasificación (rating) y el número de rentas, 
y cómo podemos utilizar esta información para optimizar nuestro inventario y estrategias de marketing?
*/

SELECT 
    f.rating,
    CASE 
        WHEN f.length <= 60 THEN 'Corta (<= 60 min)'
        WHEN f.length > 60 AND f.length <= 120 THEN 'Media (61-120 min)'
        ELSE 'Larga (> 120 min)'
    END AS duracion_categoria,
    AVG(rentas_por_pelicula) AS promedio_rentas
FROM 
    film f
JOIN 
    (SELECT 
        i.film_id, 
        COUNT(r.rental_id) AS rentas_por_pelicula
    FROM 
        inventory i
    JOIN 
        rental r ON i.inventory_id = r.inventory_id
    GROUP BY 
        i.film_id
    ) AS rentas ON f.film_id = rentas.film_id
GROUP BY 
    f.rating, duracion_categoria
ORDER BY 
    f.rating, promedio_rentas DESC;
    
    
#Pregunta 2
/*
¿Cuál es el promedio de duración de las películas por clasificación (rating)?
*/

SELECT 
    f.rating, 
    AVG(f.length) AS promedio_duracion
FROM 
    film f
GROUP BY 
    f.rating;
    
#Pregunta 3
/*
¿Cuáles son los 5 clientes que más películas han rentado y cuántas rentas ha realizado cada uno?
*/

SELECT 
    c.customer_id, 
    c.first_name, 
    c.last_name, 
    COUNT(r.rental_id) AS total_rentas
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
GROUP BY 
    c.customer_id
ORDER BY 
    total_rentas DESC
LIMIT 5;


#Pregunta 4
/*
¿Cuál es el ingreso total generado por cada tienda?
*/

SELECT 
    s.store_id, 
    SUM(f.rental_rate) AS ingreso_total
FROM 
    store s
JOIN 
    inventory i ON s.store_id = i.store_id
JOIN 
    film f ON i.film_id = f.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
GROUP BY 
    s.store_id;
    
    
#Pregunta 5
/*
¿Cuál es el top 3 de las películas más rentadas de todo el catálogo?
*/

SELECT 
    f.title, 
    COUNT(r.rental_id) AS total_rentas
FROM 
    film f
JOIN 
    inventory i ON f.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
GROUP BY 
    f.film_id
ORDER BY 
    total_rentas DESC
LIMIT 3;