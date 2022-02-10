SELECT customer.first_name as first_name, customer.last_name as last_name, customer.email as email, address.address as address FROM customer
JOIN address on address.address_id = customer.address_id 
WHERE address.city_id = 312;

SELECT film.title as title, film.description as description, film.release_year as release_year, film.rating as rating, film.special_features as special_features, category.name as genre FROM film_category
JOIN film on film.film_id = film_category.film_id 
JOIN category on category.category_id = film_category.category_id
WHERE film_category.category_id = 5;

SELECT actor.actor_id AS actor_id, CONCAT(actor.first_name," ", actor.last_name) AS actor_name, film.title AS title, film.description AS description, film.release_year AS release_year FROM film_actor
JOIN actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 5;

SELECT * FROM customer
JOIN store on store.store_id = 1
JOIN address on address.address_id = customer.address_id
WHERE address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 or address.city_id = 459


