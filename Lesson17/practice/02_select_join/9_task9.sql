SELECT Colors.name,
       COUNT(Products.id)
FROM Colors
         JOIN Products ON Colors.id = Products.color_id
GROUP BY Colors.name;