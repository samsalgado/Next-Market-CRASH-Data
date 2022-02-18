\-- Get a list of databases
SELECT datname FROM pg_database
WHERE datistemplate = false
CREATE TABLE findings(id serial PRIMARY KEY,
year VARCHAR(100) NOT NULL,
median_income VARCHAR(100));
 INSERT INTO findings (year, median_income) VALUES (1972, '27,600');
 INSERT INTO findings (year, median_income) VALUES (1976, '44,200');
 INSERT INTO findings (year, median_income) VALUES (1980, '64,600');
 INSERT INTO findings (year, median_income) VALUES (1982, '69,300');
 INSERT INTO findings (year, median_income) VALUES (1985, '84,300');
 INSERT INTO findings (year, median_income) VALUES (1988, '112,500');
 INSERT INTO findings (year, median_income) VALUES (1992, '121,500');
 INSERT INTO findings (year, median_income) VALUES (1996, '140,000');
 INSERT INTO findings (year, median_income) VALUES (2000,'169,000');
 INSERT INTO findings (year, median_income) VALUES (2004,'221,000');
 INSERT INTO findings (year, median_income) VALUES (2008,'232,100');
 INSERT INTO findings (year, median_income) VALUES (2010,'221,800');
 INSERT INTO findings (year, median_income) VALUES (2012,'245,200');
 INSERT INTO findings (year, median_income) VALUES (2014,'288,500');
 INSERT INTO findings (year, median_income) VALUES (2016,'307,800');
 INSERT INTO findings (year, median_income) VALUES (2018,'326,400');
 INSERT INTO findings (year, median_income) VALUES (2019,'321,500');
 INSERT INTO findings (year, median_income) VALUES (2020,'336,900');
INSERT INTO findings (year, median_income) VALUES (2021,'392,900');
























