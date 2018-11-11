# WRITE your MySQL query STATEMENT below
SELECT distinct(a.Email)
FROM Person AS a,
     Person AS b
WHERE a.Id<>b.Id
  AND a.Email=b.Email;

