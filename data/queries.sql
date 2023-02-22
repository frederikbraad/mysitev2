SELECT * FROM customers;
SELECT * FROM customers ORDER BY companyname ASC;
SELECT * FROM customers ORDER BY companyname DESC;
--- ASC = ascending --- desc = descending
SELECT * FROM products;
-- Aggregate functions
-- Select the cheapest product
SELECT MIN(unitprice) AS cheapest_price FROM products;
-- Select the priciest product
SELECT MAX(unitprice) AS highest_price FROM products;
-- Select the average price from all products
SELECT AVG(unitprice) FROM products;
-- Give me the total of products in the table
SELECT COUNT(*) FROM products;
-- ALIAS
SELECT COUNT(*) AS total_products FROM products;


-- Pagination (First number is where you start from, second number is how many you want)
SELECT * FROM products LIMIT 0, 5;
-- Get 5 products, ordered by cheapest to highest
SELECT * FROM products ORDER BY unitprice LIMIT 0, 5;
-- LIKE (like is friendly match, = is a precise match) (% like is wildcard)
SELECT * FROM customers WHERE contactname LIKE "mar%";
SELECT * FROM customers WHERE contactname LIKE "%er";
SELECT * FROM customers WHERE contactname LIKE "%wa%";

--- Tweet elon + message with the word elon + users with elon
--- FULL TEXT SEARCH
-- SELECT * FROM users WHERE username = "elonmusk"
-- JOIN tweets, ON users.id = tweets.user_fk

SELECT * FROM customers;
SELECT * FROM orders;

SELECT * FROM orders 
JOIN customers 
ON orders.CustomerID = customers.CustomerID
WHERE customers.customerid = "VINET" LIMIT 0,2;

--- Create a command that gives all the orders and products
-- from the user the customerid vinet

SELECT * FROM orders 
JOIN customers 
ON orders.CustomerID = customers.CustomerID
WHERE customers.customerid = "VINET" LIMIT 0,2;

SELECT * FROM orders, products 
JOIN customers
ON orders.CustomerID + products.SupplierID = customers.CustomerID
WHERE customers.customerid = "VINET";

