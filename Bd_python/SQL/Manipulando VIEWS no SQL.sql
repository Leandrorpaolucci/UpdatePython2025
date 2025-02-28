USE sakila;

-- Criando uma View, " Deixar comandos no gatilho para apenas SELECTS mais Rápidos "

CREATE VIEW vendas_por_cliente AS

SELECT
	cus.customer_id AS 'ID',
    cus.first_name AS 'Nome',
    cus.last_name AS 'Sobrenome',
    pay.amount 
	
FROM customer cus
JOIN payment pay
	ON cus.customer_id = pay.payment_id;
	
-- SELECT na View = Visualização Rapida Criada
SELECT * FROM sakila.vendas_por_cliente;

-- Removendo a Visualização Rapida
DROP VIEW vendas_por_cliente;

-- Mas caso você precise atualizar algum dado, para não fazer o drop, podemos utilizar o comando abaixo:

-- Comando para atualizar os selects em caso de alterações/updates

CREATE OR REPLACE VIEW vendas_por_cliente AS

SELECT
	cus.customer_id AS 'ID',
    cus.first_name AS 'Nome',
    cus.last_name AS 'Sobrenome',
    pay.amount
	
FROM customer cus
JOIN payment pay

	ON cus.customer_id = pay.payment_id
ORDER BY pay.amount ASC;

-- Visualizando pós/mudanças.
SELECT * FROM sakila.vendas_por_cliente;