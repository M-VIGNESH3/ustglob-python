--6.Given a table Sales(sale_id, product_id, sale_date, quantity), 
--write a query to find the total quantity sold for each product in the year 2024.

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT
);

INSERT INTO Sales VALUES
(10, 201, '2024-01-02', 10),
(20, 201, '2024-03-04', 20),
(30, 202, '2023-05-06', 15),
(40, 202, '2024-07-08', 25),
(50, 203, '2025-09-10', 5);


--solution for 6th question 
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales WHERE YEAR(sale_date) = 2024 GROUP BY product_id;