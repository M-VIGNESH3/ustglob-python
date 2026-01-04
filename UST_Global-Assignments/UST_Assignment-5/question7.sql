--7.Write an SQL query to display the top 3 highest-paid employees from each department.

-- solution for 7th question

SELECT *
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
    FROM Employees
) ranked
WHERE rnk <= 3;