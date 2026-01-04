--1.Write an SQL query to display the second highest salary from an Employees table.

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT,
    department_id INT,
    manager_id INT
);

INSERT INTO Employees VALUES
(10,'Abc',87000,10,11),
(20,'def',65000,10,11),
(30,'hij',85000,20,31),
(40,'klm',60000,10,11),
(50,'nop',83000,20,31),
(60,'qrs',55000,30,61),
(70,'tuv',92000,30,61);

--solution for question 1
SELECT MAX(salary) AS second_highest_salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);