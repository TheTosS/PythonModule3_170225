SELECT Products.name, Products.price, Colors.name
FROM Products
JOIN Colors ON Products.color_id = Colors.id
WHERE Products.name LIKE '%Pro%';
-- WHERE lower(Colors.name) = 'red';