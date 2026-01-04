--9.Write an SQL query to find employees who do not have any records in the Attendance table.

CREATE TABLE Attendance (
    employee_id INT,
    attendance_date DATE
);

INSERT INTO Attendance VALUES
(10, '2024-01-01'),
(20, '2024-01-01');

--solution 9th question

SELECT e.name FROM Employees e
LEFT JOIN Attendance a ON e.employee_id = a.employee_id
WHERE a.employee_id IS NULL;

