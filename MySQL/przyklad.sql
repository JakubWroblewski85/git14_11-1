
-- tworzenie nowej tabeli
CREATE TABLE agenci2 (
    agentid INT,
    agentname VARCHAR(50),
    waznosclicencji DATETIME(6)
);

insert into agenci2 values (007, 'Sylwia Kotecka', '2020-12-20 00:00:00');

SELECT 
    *
FROM
    agenci2;

INSERT INTO agenci2 VALUES
(2, 'Anna Pieskowa', '2023-12-31 00:00:00'),
(3, 'Janusz Mysicki', '2019-11-11 0:00:00');

--
COMMIT;


INSERT INTO agenci2 VALUES
(null, 'Janusz Mysicki', '2025-12-15 00:00:00');

-- pokaze nam ilosc osob
SELECT count(*) FROM alk.agenci2;

CREATE TABLE agenci2_kopia AS SELECT * FROM
    agenci2;

SELECT 
    *
FROM
    agenci2_kopia;
    
-- wyswietli nam wszystkie wszsytkie
SELECT 
    *
FROM
    agenci2
WHERE
    agentid = 7;
    
-- 19 Pobierz id agentów o imionach nie kończących się na -a.
SELECT agentid FROM agenci2 WHERE agentname NOT LIKE '%a %';


CREATE TABLE klienci (
    klientid INT,
    klientname NVARCHAR(50),
    adres NVARCHAR(80),
    pesel DOUBLE PRECISION,
    plec CHAR(1),
    dataur DATE
);

SELECT * FROM klienci;

-- 23
ALTER TABLE klienci
CHANGE COLUMN klientid
klientid INT NOT NULL AUTO_INCREMENT, ADD PRIMARY KEY (klientid);

-- 24
ALTER TABLE klienci 
CHANGE COLUMN pesel 
pesel DOUBLE PRECISION UNIQUE;

-- 25
INSERT INTO klienci VALUES
(null, 'Andrzej Małpiński', 'ul. Szcęśliwa 7, 61-001 Poznań', 89060412345, 'M', '2019-11-11 0:00:00'),
(null, 'Aneta Tygrysicka', 'ul. Poznańska 100, 02-002 Warszawa', 80060812345, 'K', '2010-12-01 0:00:00');

SELECT * FROM klienci;

-- 28
UPDATE klienci SET klientname = 'Krzysztof Małpiński' WHERE klientid=3;

-- 29, 30, 31
insert into klienci values
(NULL, 'Joanna Skowrońska', 'ul. 26 Kwietnia 200/10, 70-100 Szczecin', 79050300102, 'K', '1979-03-02'),
(null, 'Anna Pingwinowska', '', 77031300506, 'K', '1977-03-13'),
(null, 'Maciej Lemur', 'ul. Zoologiczna, 60-600 Poznań', 99082310101, 'M', '1999-08-23');

COMMIT;

-- 32
SELECT * FROM klienci where adres like '%Poznań';


-- 33
select * from klienci where dataur <'1986-12-11';

-- 34
select * from klienci where klientid <>2;
select * from klienci where klientid !=2;


-- 35
select * from klienci order by klientname;

-- 36
select * from klienci order by dataur desc;

-- 37
select * from klienci limit 0,2;


-- 38
CREATE TABLE kliencikopiaK AS SELECT * FROM
    klienci
WHERE
    plec = 'K';
    
    
SELECT * FROM kliencikopiaK;

-- 39
DELETE FROM kliencikopiaK 
WHERE
    adres LIKE '%Szczecin%';
    
-- aby usunąć baze po błedzie wchodzimy do -edit -Preference -SQL Editor 
-- na samym dole odznaczamy boxa i wchodzimy -Query reconected to serwer

commit;

SELECT * FROM klienci UNION SELECT * FROM kliencikopiaK;


-- 41
ALTER TABLE kliencikopiaK ADD COLUMN wiek INT;

-- 42
ALTER TABLE kliencikopiaK DROP COLUMN wiek;

-- 43
DELETE FROM kliencikopiaK WHERE klientid=2;

-- 44
TRUNCATE TABLE kliencikopiaK;

-- 45
CREATE TABLE polisy (
numerpolisy INT NOT NULL UNIQUE,
rodzajubezpieczenia INT,
klientid INT,
agent INT,
kwota FLOAT,
terminplatnosci DATE,
zaplacono BOOLEAN
);

-- 46
insert into polisy values
(15301, 3, 6, 3, 100.50, '2020-01-01', 1),
(15302, 2, 5, 3, 200.00, '2020-12-01', 0),
(15303, 2, 1, 1, 50.55, '2019-10-01', 1),
(15305, 1, 2, 2, 99.99, '2020-01-01', 1),
(15306, 1, 4, 2, 1000.00, '2020-02-01', 0),
(15307, 2, 3, 3, 15.45, '2019-12-01', 0);

-- 47
create table rodzajeubezp(
rodzajid int,
rodzaj nvarchar(50));

-- 48
insert into rodzajeubezp values
(1, 'autocasco'),
(2, 'OC'),
(3, 'mieszkanie');

commit;

SELECT * FROM polisy;

-- 50
SELECT * FROM
polisy p
JOIN
rodzajeubezp r ON p.rodzajubezpieczenia = r.rodzajid;

-- 51
SELECT
    p.numerpolisy AS 'NUMER POLISY',
    p.kwota,
    p.terminplatnosci,
    r.rodzaj AS RODZAJ
FROM
    polisy p
        JOIN
    rodzajeubezp r ON p.rodzajubezpieczenia = r.rodzajid;


-- 52
SELECT 
    p.numerpolisy,
    p.rodzajubezpieczenia,
    k.klientname,
    p.agent,
    p.kwota,
    p.terminplatnosci,
    p.zaplacono
FROM
    polisy p
        JOIN
    klienci k ON p.klientid = k.klientid;
    
-- 53
SELECT
    p.numerpolisy,
    p.rodzajubezpieczenia,
    k.klientname,
    a.agentname,
    p.kwota,
    p.terminplatnosci,
    p.zaplacono
FROM
    polisy p
        JOIN
    klienci k ON p.klientid = k.klientid
        JOIN
    agenci2 a ON p.agent = a.agentid;
    
    
-- 54
SELECT
    p.numerpolisy AS 'NUMER POLISY',
    k.klientname,
    a.agentname,
    p.kwota,
    p.terminplatnosci,
    p.zaplacono,
    r.rodzaj AS RODZAJ
FROM
    polisy p
        JOIN
    rodzajeubezp r ON p.rodzajubezpieczenia = r.rodzajid   -- 54
        JOIN
    klienci k ON p.klientid = k.klientid
        JOIN
    agenci2 a ON a.agentid = p.agent;

-- 55
SELECT
    p.numerpolisy AS 'NUMER POLISY',
    k.klientname AS 'KLIENT',
    a.agentname AS 'AGENT',
    p.kwota AS 'KWOTA',
    p.terminplatnosci AS 'TERMIN PŁATNOŚCI',
    p.zaplacono AS 'ZAPŁACONO',
    r.rodzaj AS 'RODZAJ UBEZPIECZENIA'
FROM
    polisy p
        JOIN
    rodzajeubezp r ON p.rodzajubezpieczenia = r.rodzajid   -- 54
        JOIN
    klienci k ON p.klientid = k.klientid
        JOIN
    agenci2 a ON a.agentid = p.agent;

-- 56
-- aby stworzyc widok trzeba wpisac create view i nazwe widoku
CREATE VIEW poliski AS
    SELECT 
        p.numerpolisy AS 'NUMER POLISY',
        k.klientname AS 'KLIENT',
        a.agentname AS 'AGENT',
        p.kwota AS 'KWOTA',
        p.terminplatnosci AS 'TERMIN PŁATNOŚCI',
        p.zaplacono AS 'ZAPŁACONO',
        r.rodzaj AS 'RODZAJ UBEZPIECZENIA'
    FROM
        polisy p
            JOIN
        rodzajeubezp r ON p.rodzajubezpieczenia = r.rodzajid
            JOIN
        klienci k ON p.klientid = k.klientid
            JOIN
        agenci2 a ON a.agentid = p.agent;

commit;


SELECT hello('world2');


