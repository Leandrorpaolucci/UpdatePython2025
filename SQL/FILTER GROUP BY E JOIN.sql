-- FILTER

USE sakila;

SELECT * FROM sakila.payment;

SELECT 
	MAX(amount) AS 'Maior Valor Vendido',
	MIN(amount) AS 'Menor Valor Vendido',
	AVG(amount) AS 'Média de Valores',
    SUM(amount) AS 'Soma total de Vendas',
    COUNT(amount) AS 'Quantidade de vendas desde o inicio'
	
FROM payment
WHERE staff_id = 2

-- GROUP BY
SELECT 
	customer_id,
    SUM(amount) AS Total
	
FROM payment
GROUP BY customer_id
ORDER BY total DESC


-- GROUP BY + JOIN
SELECT
	cus.customer_id AS 'ID',
    cus.first_name AS 'Nome',
    cus.last_name AS 'Sobrenome', 
    SUM(amount) AS 'Total'
    
FROM payment pay
JOIN customer cus USING(customer_id)

GROUP BY customer_id
ORDER BY total DESC;


