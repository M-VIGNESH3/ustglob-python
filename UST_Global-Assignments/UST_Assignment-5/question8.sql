--8.Given a table Customers(customer_id, customer_name, city), write a query to find cities that have more than 5 customers.

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO Customers VALUES
(1,'A','Delhi'),
(2,'B','Delhi'),
(3,'C','Delhi'),
(4,'D','Delhi'),
(5,'E','Delhi'),
(6,'F','Delhi'),
(7,'G','Mumbai');

--solution 8th question 
SELECT city FROM Customers
GROUP BY city HAVING COUNT(*) > 5;