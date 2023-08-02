'Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)'
SELECT * FROM orders
ORDER BY required_date DESC, shipped_date ASC;

'Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA'
SELECT AVG(shipped_date - order_date) AS middle_day
FROM orders
WHERE ship_country = 'USA';

'Найти сумму, на которую имеется товаров (количество * цену) причём таких,
которые не сняты с продажи (см. на поле discontinued)'
SELECT SUM(unit_price * units_in_stock) AS poduct_sum
FROM products
WHERE discontinued <> 1;