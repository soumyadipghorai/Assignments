--? SELECT 
SELECT * FROM film;

-- SELECT col_name1, col_name2,... FROM table_name 

--* first it goes for the table name --> col name 
--  * means all the cols from a table 


SELECT last_name, first_name FROM actor;

--? DISTINCT
SELECT first_name, last_name, email FROM customer;
SELECT DISTINCT(first_name, last_name, email) FROM customer; -- only distinct values 


--? COUNT
SELECT COUNT(*) FROM film; -- counts the number of rows 
--* COUNT is a function so () is must after COUNT

SELECT COUNT(DISTINCT(film_id)) FROM film; -- counts the distinct film_id 

--!  <> == != 

--? WHERE 

SELECT name, choice FROM table 
WHERE name = 'David' AND choice = 'Red'

-- count the number of rows satisfying the conditions 
SELECT COUNT(*) FROM film
WHERE rental_rate > 4 AND replacement_cost >= 19.99
AND rating = 'R'

SELECT first_name, last_name, email FROM customer
WHERE first_name = 'Nancy' AND last_name = 'Thomas';

SELECT description FROM film 
WHERE title = 'Outlaw Hanky';

SELECT phone FROM address
WHERE address = '259 Ipoh Drive';

--? ORDER BY
SELECT column_1, column_2 
FROM table 
ORDER BY column_1, column_2 ASC/DESC -- ascendin/descending --> order by comes at last --> ascending by default 

SELECT store_id, first_name, last_name FROM customer 
ORDER BY store_id DESC, first_name ASC;

--? LIMIT  

SELECT * FROM payment
WHERE amount != 0.00
ORDER BY payment_date DESC
LIMIT 5;

SELECT customer_id FROM payment
WHERE amount > 0
ORDER BY payment_date 
LIMIT 10;

SELECT title FROM film
ORDER BY length 
LIMIT 5;

SELECT COUNT(title) FROM film
WHERE length <= 50;

-- ? BETWEEN 8 AND 9 --> 8,9 --> NOT BETWEEEN 8 AND 9 --> ...7,10...

SELECT COUNT(*) FROM payment 
WHERE amount NOT BETWEEN 8 AND 9;

SELECT * FROM payment 
WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-15'; -- if you do 14 then you won't get any ans as the date starts at 00:01:00 

-- ? IN / NOT IN
-- if a value is in a list 

SELECT COUNT(*) FROM payment
WHERE amount NOT IN (0.99,1.98,1.99)

SELECT * FROM customer 
WHERE first_name NOT IN ('John', 'Jake','Julie')
ORDER by customer_id
LIMIT 10;

-- ? LIKE & ILIKE

-- WHERE name LIKE 'A%' --> starts with 'A
-- WHERE name LIKE '%a' --> ends with 'a'  --> LIKE is case-sensitive 
-- ILIKE is case-insensitive

-- ! % and _ are the wildcards
-- WHERE value LIKE 'version# _ _'  --> anything in the _

--* WHERE name LIKE '_her%' --> C her yl, T her esa, S her ri

SELECT * FROM customer
WHERE first_name ILIKE 'J%' AND last_name ILIKE 's%';

SELECT * FROM customer
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name;

-- ? challenges 

SELECT COUNT(*) FROM payment
WHERE amount > 5.00;

SELECT COUNT(first_name) FROM actor
WHERE first_name LIKE 'P%';

SELECT COUNT(DISTINCT(district)) FROM address;

SELECT DISTINCT(district) FROM address;

SELECT COUNT(*) FROM film
WHERE rating = 'R' 
AND replacement_cost BETWEEN 5 AND 15;

SELECT COUNT(*) FROM film
WHERE title LIKE '%Truman%';


-- ? AGGREGATE 

-- AVG() COUNT() MAX() MIN() SUM()

SELECT MIN(replacement_cost) FROM film;

SELECT MAX(replacement_cost) FROM film;
-- if you use multiple col it will give an error as max gives a single value 
SELECT MIN(replacement_cost), MIN(replacement_cost) FROM film;

SELECT COUNT(*) FROM film;

SELECT ROUND(AVG(replacement_cost),3) FROM film;
-- AVG gives a lot of digits after . --> so we use round to specify the no of places after decimal 
SELECT SUM(replacement_cost) FROM film;



-- ? GROUP BY 
-- ------------------------        -------------
-- A          |     10    |         A        10              --------------------
-- A          |      5    |         A         5             |  A             15 |
-- B          |      2    |        -------------            |-------------------|
-- B          |      4    |   -->   B         2   SUM -->   |  B             6  |
-- C          |     12    |         B         4             |-------------------|
-- C          |      6    |        -------------            |  C            18  |
-- ------------------------         C        12             ---------------------
--                                  C         6
                                   --------------


SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC;

SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY customer_id

SELECT DATE(payment_date), SUM(amount) FROM payment
GROUP BY DATE(payment_date) 
ORDER BY SUM(amount) DESC
-- date makes the date time to date 

SELECT staff_id, COUNT(amount) FROM payment 
GROUP BY staff_id 
ORDER BY COUNT(amount) DESC;

SELECT rating, ROUND(AVG(replacement_cost),3) FROM film
GROUP BY rating
ORDER BY AVG(replacement_cost) DESC;

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5;

-- ? HAVING 

SELECT company, SUM(sales) FROM finance_table 
WHERE company != 'Google'
GROUP BY company
HAVING SUM(sales) > 1000;

SELECT customer_id, SUM(amount) FROM payment
WHERE customer_id NOT IN (184, 87, 477)
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY SUM(amount) DESC
LIMIT 10;

SELECT store_id, COUNT(customer_id) FROM customer
GROUP BY store_id
HAVING COUNT(customer_id) > 300;

SELECT customer_id, COUNT(amount) FROM payment
WHERE amount > 0.00
GROUP BY customer_id
HAVING COUNT(amount) >= 40
ORDER BY COUNT(amount) DESC

SELECT customer_id, SUM(amount) FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY SUM(amount) DESC;


-- ? RIGHT 

SELECT NAME FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME, 3), ID ASC;

SELECT customer_id FROM payment
WHERE staff_id = 2
GROUP BY customer_id 
HAVING SUM(amount) >= 110;

SELECT COUNT(title) FROM film
WHERE title LIKE 'J%';

SELECT * FROM customer
WHERE address_id < 500 AND first_name LIKE 'E%'
ORDER BY customer_id DESC;

-- ? JOINS 

-- ? AS (rename) 
-- executed at end 
SELECT amount AS rental_price FROM payment;

SELECT customer_id, SUM(amount) AS total_spent -- rename the sum col 
FROM payment
GROUP BY customer_id

SELECT customer_id, SUM(amount)  AS total_spent
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY total_spent;
-- if you use HAVING total_spent it will give an error but after order by you can use 

SELECT customer_id, amount AS new_name
FROM payment
WHERE amount > 2; -- same for WHERE

-- ? INNER JOIN 
-- A intersection B
-- match values from column available in both table 
SELECT payment_id, payment.customer_id, first_name FROM payment 
INNER JOIN customer 
ON payment.customer_id = customer.customer_id
-- payment_id comes once in payment table 
-- customer_id comes in both 
-- first_name comes once in customer table 

-- ? OUTTER JOIN
-- A union B
-- consider both common and uncommon 
SELECT * FROM customer
FULL OUTER JOIN payment 
ON customer.customer_id = payment.customer_id 
WHERE customer.customer_id IS null 
OR payment.payment_id IS null;
-- no customer who never made a payment and no payment info not associated with no customer 

-- ? LEFT OUTER JOIN
-- A --> order matters
SELECT film.film_id, film.title, inventory_id, store_id FROM film
LEFT OUTER JOIN inventory ON 
inventory.film_id = film.film_id
WHERE inventory.film_id IS NULL;
-- Shows the things that we don't have in our inventory 

-- ? RIGHT OUTER JOIN 
-- B

SELECT district, email FROM address 
INNER JOIN customer ON 
address.address_id = customer.address_id
WHERE district = 'California';

SELECT title, first_name, last_name FROM actor 
INNER JOIN film_actor ON
actor.actor_id = film_actor.actor_id
INNER JOIN film ON 
film.film_id = film_actor.film_id
WHERE actor.first_name = 'Nick' AND actor.last_name = 'Wahlberg';
-- where comes after join 

-- ? TIME

SHOW TIMEZONE;

SELECT NOW()

SELECT TIMEOFDAY()

SELECT CURRENT_TIME
SELECT CURRENT_DATE

SELECT EXTRACT(QUARTER FROM payment_date) 
AS my_year FROM payment;

SELECT AGE(payment_date) FROM payment

SELECT TO_CHAR(payment_date, 'MONTH-YYYY') FROM payment;
SELECT TO_CHAR(payment_date, 'MM/DD/YYYY') FROM payment;