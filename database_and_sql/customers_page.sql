'Посчитать количество заказчиков'
SELECT COUNT(1) FROM customers;

'Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики'
SELECT DISTINCT city, country FROM customers;

'Найти заказчиков и обслуживающих их заказы сотрудников, таких,
что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express.
Вывести компанию заказчика и ФИО сотрудника.'
SELECT customers.company_name, CONCAT(employees.first_name, ' ', employees.last_name) AS full_name 
FROM orders
INNER JOIN customers USING(customer_id)
INNER JOIN employees USING(employee_id)
JOIN shippers ON orders.ship_via=shippers.shipper_id
WHERE employees.city ='London' AND customers.city='London' 
AND shippers.company_name = 'Speedy Express';

'Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.'
SELECT company_name
FROM customers
WHERE NOT EXISTS (SELECT customer_id FROM orders WHERE customers.customer_id = orders.customer_id)