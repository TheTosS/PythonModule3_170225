SELECT *
FROM Products
WHERE Price > 500;

SELECT *
FROM Products
WHERE Price > 500 AND StockQuantity > 100;

SELECT *
FROM Products
WHERE Price BETWEEN 100 AND 500;