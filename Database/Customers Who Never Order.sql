# WRITE your MySQL query STATEMENT below
SELECT Name AS Customers
FROM Customers AS a
WHERE a.Id NOT IN
    (SELECT CustomerId
     FROM Orders);

