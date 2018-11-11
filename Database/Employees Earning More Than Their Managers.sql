# WRITE your MySQL query STATEMENT below
SELECT a.name
FROM Employee a
INNER JOIN Employee b ON a.managerId=b.Id
AND a.Salary>b.Salary;

# Faster
SELECT a.name
FROM Employee a,
     Employee b
WHERE a.managerId=b.Id
  AND a.Salary>b.Salary;

