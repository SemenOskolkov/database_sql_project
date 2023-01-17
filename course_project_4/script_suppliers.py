import json
import psycopg2

with psycopg2.connect(
        host='localhost',
        database='Northwind Traders',
        user='postgres',
        password='8071'
) as conn:
    with conn.cursor() as cur:
        with open('suppliers.json', 'r', encoding='utf-8') as file:  # Работа с файлом suppliers.json
            suppliers_file = json.load(file)
            for row in suppliers_file:
                cur.execute(
                    "INSERT INTO suppliers(company_name, contact_name, contact_title, country, region, postal_code, city, address, phone, fax, homepage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (row.get("company_name"), row.get("contact").split(',')[0], row.get("contact").split(',')[1],
                     row.get("address").split(';')[0], row.get("address").split(';')[1],
                     row.get("address").split(';')[2], row.get("address").split(';')[3],
                     row.get("address").split(';')[4],
                     row.get("phone"), row.get("fax"), row.get("homepage")))  # Заполнение данных в таблицу

conn.close()