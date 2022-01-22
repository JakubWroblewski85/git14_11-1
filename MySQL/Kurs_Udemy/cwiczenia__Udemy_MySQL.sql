USE najszybsze_zwierzeta;


SELECT * FROM najwolniejsze_zwierzeta;

SHOW tables;

CREATE TABLE najwolniejsze_zwierzeta (
    zwierze CHAR(20),
    gatunek CHAR(10),
    predkosc INT
);

DROP table najwolniejsze_zwierzeta;

INSERT INTO najwolniejsze_zwierzeta values
('Stonka Amerykanska', 'ptak', 8.0),
('Zolw Wielki', 'gad', 1.6),
('Konik Morski', 'ryba', 0.0161),
('Slimak Bananowy', 'gad', 0.000083);