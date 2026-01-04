--5.Write an SQL query to retrieve the names of employees who earn more than the average salary of their department.

--solution 5th qustion 

SELECT e.name FROM Employees e WHERE e.salary >
(SELECT AVG(salary) FROM Employees WHERE department_id = e.department_id );
