USE sakila;

--SubSELECT

SELECT * 
FROM payment
WHERE amount > (SELECT AVG(amount)	FROM payment)

-- EX II SubSelect
SELECT *
FROM payment
WHERE amount = (SELECT MAX(amount) FROM payment WHERE customer_id = 1);


-- EX III SubSELECT
SELECT *
FROM customer
WHERE customer_id IN (SELECT customer_id AS 'ID' FROM payment
	GROUP BY customer_id
	HAVING COUNT(*) > 35)
	
	

