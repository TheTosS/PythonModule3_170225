-- 1
SELECT ProductName, Price, StockQuantity
FROM Products
WHERE StockQuantity < 50;

-- 2
SELECT *
FROM Products
WHERE Price > 5000 AND StockQuantity > 30;

-- 4
SELECT *
FROM Products
WHERE ProductName LIKE '%USB%' OR ProductName LIKE '%Bluetooth%';

-- 5
SELECT ProductName, Price
FROM Products
WHERE ProductName NOT LIKE '%Монитор%'
  AND ProductName NOT LIKE '%Наушники%'
  AND Price > 10000;