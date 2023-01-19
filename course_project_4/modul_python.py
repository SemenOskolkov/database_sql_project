import json
import psycopg2


def get_product_by_id(config=None, id=None):  # Получение данных по продуктам
    cur = config.cursor()
    cur.execute(
        "SELECT product_id, product_name, categories.category_name, unit_price FROM products JOIN categories USING(category_id)")
    product_catalog = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]

    cur.connection.close()
    return product_catalog[id-1]


object_id = int(input('Введите id для получения информации по продукту: '))
product_conn = get_product_by_id(
    config=psycopg2.connect(host='localhost', database='Northwind Traders', user='postgres', password='8071'),
    id=object_id)  # Передаем подключение к БД и индекс от пользователя

product_data = json.dumps(product_conn)
print(product_data)


def get_category_by_id(config=None, id=None):  # Получение данных по категориям
    cur = config.cursor()
    cur.execute(
        "SELECT category_id, category_name, description, products.product_name FROM categories JOIN products USING(category_id)")
    category_product = [dict((cur.description[i][0], value)  # Получаем массив словарей с product_name
                            for i, value in enumerate(row)) for row in cur.fetchall()]
    # print(category_product)

    cur.execute(
        "SELECT category_id, category_name, description FROM categories")
    category_catalog = [dict((cur.description[i][0], value)  # # Получаем массив словарей без product_name
                             for i, value in enumerate(row)) for row in cur.fetchall()]
    # print(category_catalog)

    for j in category_catalog:  # Дособираем category_catalog со списком товаров в категории
        j['product_name'] = []
        for i in category_product:
            if i.get('category_name') == j.get('category_name'):
                j['product_name'].append(i.get('product_name'))

    cur.connection.close()
    return category_catalog[id-1]


object_id = int(input('Введите id для получения информации по категории: '))
category_conn = get_category_by_id(
    config=psycopg2.connect(host='localhost', database='Northwind Traders', user='postgres', password='8071'),
    id=object_id)  # Передаем подключение к БД и индекс от пользователя

category_data = json.dumps(category_conn)
print(category_data)
