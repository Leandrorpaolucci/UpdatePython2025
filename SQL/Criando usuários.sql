-- Visualizando os usuarios
SELECT * FROM mysql.user;

-- criando usuario com privilegios

CREATE USER leandro IDENTIFIED BY'1212';

CREATE USER Camila@localhost IDENTIFIED BY '1212';

CREATE USER Cecilia@natural.com identified by '1212';

-- removendo usuarios
DROP USER Cecilia@natural.com;

-- recuperando a senha de usuarios

SELECT * FROM mysql.user;

SET password FOR Camila@localhost = '123456'; -- alterando senha de usuarios
-- alterando a minha propria senha 

SET password  = '123456'; -- usuario logado

-- trabalhando com privilegios

-- SHOW GRANTS FOR leandro; verifica os privilegios
-- SELECT * FROM mysql.user; verifica os privilegios detalhados

-- Habilitando privilegios aos usuários

GRANT SELECT, INSERT, UPDATE, DELETE
ON sakila.*
TO leandro;

-- Após permitir os privilegios com comandos acima, verificamos abaixo:
SHOW GRANTS FOR leandro;

-- Adicionando um administrador / admin
-- "promovendo as pessoas como admin" -- ter todos os privilegios database sakila

GRANT ALL 
ON sakila.*
TO leandro;
SHOW GRANTS FOR leandro;
SELECT * FROM mysql.user;

-- Promovendo privilegios a todas as databases

GRANT ALL 
ON *.*
TO Camila@localhost;
SELECT * FROM mysql.user;
SHOW GRANTS FOR Camila@localhost;

-- Removendo privilegios de usuários utilizando REVOKE

-- Criando usuario
CREATE USER Cecilia
IDENTIFIED BY '1212';

-- Verificando os acessos padrões
SHOW GRANTS FOR Cecilia;

-- Concedendo acessos
GRANT SELECT, INSERT, UPDATE
ON sakila.*
TO Cecilia;

-- Verificando os novos acessos
SHOW GRANTS FOR Cecilia;

-- Removendo o update (acesso)

REVOKE UPDATE
ON sakila.*
FROM Cecilia;

-- Verificando a remoção dos acessos
SHOW GRANTS FOR Cecilia;