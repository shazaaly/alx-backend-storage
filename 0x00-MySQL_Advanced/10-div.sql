-- Active: 1695137323808@@127.0.0.1@3306@holberton
-- a SQL script that creates a function SafeDiv that divides
-- (and returns) the first by the second number
-- returns 0 if the second number is equal to 0.


DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,5)
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$

DELIMITER ;