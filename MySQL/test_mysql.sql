
CREATE TABLE agenci (
    agenci INT,
    agentname VARCHAR(50),
    waznosclicencji DATETIME(6)
);

SELECT * FROM agenci;

INSERT INTO agenci VALUES 
(007, 'Sylwia Potocka', '2020-12-29 00:00:00');

USE alk2;
USE alk;


INSERT INTO agenci VALUES 
(00000003, 'Teresa Rudzikowska', '2021-10-30 00:00:00'),
(00002, 'Robert Moczulski', '2019-08-18 0:00:00');

commit;

ALTER TABLE agenci CHANGE COLUMN agentid agentid INT(11) NOT NULL AUTO_INCREMENT, ADD PRIMARY KEY (agentid);

-- 15
CREATE TABLE agenci_kopia AS SELECT * FROM
    agenci;

-- 16
SELECT * FROM agenci WHERE agentid = 7;

-- 17
SELECT * FROM agenci WHERE agentname LIKE'%a';

-- 18
SELECT * FROM agenci WHERE agentname NOT LIKE'%a';

-- 19
SELECT * FROM agenci WHERE agentname LIKE'%a';

-- 20
SELECT * FROM agenci WHERE agentname LIKE'%a';

-- 
show databases;




