--10.Given a table Employees(employee_id, name, manager_id), 
--write an SQL query to display each employee’s name along with their manager’s name.


CREATE TABLE Manager(
manager_id INT,
manager_name Varchar(50));

INSERT INTO Manager VALUES 
(11, 'rana'),
(31, 'rani'),
(61, 'raju');

--solution 10th question 
SELECT e.name AS employee_name, m.manager_name AS manager_name
FROM Employees e, Manager m
WHERE e.manager_id = m.manager_id

