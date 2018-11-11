# WRITE your MySQL query STATEMENT below
SELECT a.Id
FROM Weather a
INNER JOIN Weather b ON datediff(a.Date,b.Date)=1
AND a.Temperature>b.Temperature;

 #
SELECT a.Id
FROM Weather AS a,
     Weather AS b
WHERE datediff(a.Date,b.Date)=1
  AND a.Temperature>b.Temperature;

