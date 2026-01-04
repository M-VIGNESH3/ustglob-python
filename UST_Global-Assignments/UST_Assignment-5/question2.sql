--2.Given a table Orders(order_id, customer_id, order_date, amount), write a query to find the total order amount per customer, 
--but display only customers whose total exceeds 50,000.

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount INT
);

INSERT INTO Orders VALUES
(1, 101, '2025-11-8', 20000),
(2, 101, '2025-02-16', 35000),
(3, 102, '2025-02-8', 15000),
(4, 103, '2025-10-03', 60000),
(5, 104, '2025-10-05', 50000);

--solution for 2n question
SELECT customer_id, SUM(amount) AS total_amount
FROM Orders
GROUP BY customer_id
HAVING SUM(amount) > 50000;