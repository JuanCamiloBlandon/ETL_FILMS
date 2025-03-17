CREATE DATABASE FILM_DATABASE;
USE FILM_DATABASE;

-- Tabla store
CREATE TABLE store (
    store_id TINYINT PRIMARY KEY,
    manager_staff_id TINYINT,
    address_id SMALLINT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla customer
CREATE TABLE customer (
    customer_id SMALLINT PRIMARY KEY,
    store_id TINYINT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    email VARCHAR(50),
    address_id SMALLINT,
    active BOOLEAN,
    create_date DATETIME,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);

-- Tabla film
CREATE TABLE film (
    film_id SMALLINT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    release_year YEAR,
    language_id TINYINT,
    original_language_id TINYINT,
    rental_duration TINYINT,
    rental_rate DECIMAL(4,2),
    length SMALLINT,
    replacement_cost DECIMAL(5,2),
    rating ENUM('G', 'PG', 'PG-13', 'R', 'NC-17'),
    special_features SET('Trailers', 'Commentaries', 'Deleted Scenes', 'Behind the Scenes'),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla inventory
CREATE TABLE inventory (
    inventory_id MEDIUMINT PRIMARY KEY,
    film_id SMALLINT,
    store_id TINYINT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (film_id) REFERENCES film(film_id),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);

-- Tabla rental
CREATE TABLE rental (
    rental_id INT PRIMARY KEY,
    rental_date DATETIME,
    inventory_id MEDIUMINT,
    customer_id SMALLINT,
    return_date DATETIME,
    staff_id TINYINT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
