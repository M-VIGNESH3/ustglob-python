--3.Write an SQL query to find the number of employees in each department, excluding departments with fewer than 3 employees.
--solution for 3rd question
SELECT customer_id, SUM(amount) AS total_amount
FROM Orders
GROUP BY customer_id
HAVING SUM(amount) > 50000;