# WRITE your MySQL query STATEMENT below
SELECT max(Salary)
FROM Employee
WHERE Salary<
    (SELECT max(Salary)
     FROM Employee);

