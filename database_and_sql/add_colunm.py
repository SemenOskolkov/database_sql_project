import json
import os

import psycopg2
from psycopg2.extras import DictCursor

with psycopg2.connect(
        host='localhost',
        database='Northwind_Traders',
        user=os.getenv('PSQL_USER'),
        password=os.getenv('PSQL_PASSWORD'),
) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT product_id, product_name FROM products ")
        product_catalog = [dict((cur.description[i][0], value)
                                for i, value in enumerate(row)) for row in
                           cur.fetchall()]  # Получаем массив словарей из БД. В словаре (ключ - название колонки, значение - данные колонки)

    with open('data/suppliers.json', 'r', encoding='utf-8') as file:  # Работа с файлом suppliers.json
        suppliers_file = json.load(file)
        product_list = []  # Получаем массив со списками из наименований продуктов
        for item in suppliers_file:
            product_list.append(item.get("products"))

    for i in product_catalog:  # Находим совпадение по названиям и дополняем массив словарей значением (индексом списка из массива) в котором было совпадение
        for j in range(len(product_list)):
            if i.get("product_name") in product_list[j]:
                i["suppliers_id"] = str(j + 1)
    # print(product_catalog)

    with conn.cursor() as cur:
        cur.execute('ALTER TABLE products ADD COLUMN supplier_id int REFERENCES suppliers')  # Добавляем колонку к таблице и делаем связь

    with conn.cursor() as cur:
        for row in product_catalog:
            cur.execute('UPDATE products SET supplier_id = %s WHERE product_id = %s ',
                        (row.get('suppliers_id'), str(row.get('product_id'))))  # Обновляем данные колонки через обновленный массив словарей

conn.close()
