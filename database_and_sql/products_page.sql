'Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood,
которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже,
имя контакта поставщика и его телефонный номер'
SELECT product_name, units_in_stock, suppliers.contact_name, suppliers.phone, discontinued, categories.category_name
FROM products
JOIN suppliers USING(supplier_id)
JOIN categories USING(category_id)
WHERE discontinued <> 1 AND units_in_stock < 20
AND categories.category_name IN ('Beverages', 'Seafood')