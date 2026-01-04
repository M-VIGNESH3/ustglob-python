--4.Given tables Students(student_id, name) and Marks(student_id, subject, marks),
--write a query to find students who have scored more than 80 in at least two subjects.

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);


INSERT INTO Students VALUES
(10, 'abc'),
(20, 'def'),
(30, 'hij'),
(40, 'klm');


CREATE TABLE Marks (
    student_id INT,
    subject VARCHAR(50),
    marks INT
);

INSERT INTO Marks VALUES
(10, 'Math', 55),
(10, 'Science', 65),
(10, 'English', 70),
(20, 'Math', 88),
(20, 'Science', 83),
(30, 'Math', 75),
(40, 'Math', 35),
(40, 'English', 40);

--solution for 4th question
SELECT student_id ,name FROM Students 
where student_id  IN (SELECT student_id FROM Marks WHERE Marks > 80 GROUP BY student_id HAVING COUNT(subject) >= 2);