SELECT Products.name AS name, Products.price AS price, Colors.name AS color
FROM Products
JOIN Colors ON Products.color_id = Colors.id
WHERE Colors.id=1;