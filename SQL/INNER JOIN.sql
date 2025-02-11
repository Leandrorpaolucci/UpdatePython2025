-- INNER JOIN

SELECT 
	customer.customer_id AS "ID",
	customer.first_name AS "Primeiro Nome",
	customer.last_name AS "Sobrenome",
	payment.payment_id AS "ID pagamento",
	payment.amount AS "Valor Pago"
	
FROM customer 
JOIN payment ON customer.customer_id = payment.payment_id

-- Multiplas tabelas

SELECT 
	customer.customer_id AS "ID",
	customer.first_name AS "Primeiro Nome",
	customer.last_name AS "Sobrenome",
	adr.address AS "Endereço", 
	payment.payment_id AS "ID pagamento",
	payment.amount AS "Valor Pago"
FROM customer 
JOIN payment 
	ON customer.customer_id = payment.payment_id
JOIN address adr 
	ON customer.customer_id = adr.address_id


