## Базы данных и SQL запросы

### Описание проекта

Проект представляет собой работу с SQL запросами с базой данных в PostgreSQL.

#### Содержание проекта

Директория **"data"** :

**"fill_db.sql"** - скрипт для наполнения текущей БД Northwind Traders.

**"suppliers.json"** - документ с данными для таблицы suppliers.

Директория **"database_and_sql"** :

**"add_colunm.py"** - содержит код по работе с таблицей products: добавление и обработка данных;

**"create_table_suppliers.sql"** - содержит скрипт по созданию таблицы suppliers в PostgreSQL;

**"customers_page.sql"** - содержит SQL запросы в PostgreSQL;

**"employees_page.sql"** - содержит SQL запросы в PostgreSQL;

**"modul_python.py"** - python-модуль для работы с БД;

**"orders_page.sql"** - содержит SQL запросы в PostgreSQL;

**"products_page.sql"** - содержит SQL запросы в PostgreSQL;

**"script_suppliers.py"** - скрипт по заполнению в БД таблицы suppliers из "suppliers.json".

### Основные системные требования:

* Python ^3.10
* Poetry 0.1.0
* PostgreSQL ^12

### Установка необходимого ПО

#### Установка Poetry

https://python-poetry.org/docs/

#### Установка PostgreSQL

https://www.postgresql.org/download/

Работа с проектом происходит через PostgreSQL и pgAdmin, но можно работать через терминал и командную строку.

### Запуск проекта

1. Загрузите проект из Github, воспользовавшись командой

```
git clone git@github.com:SemenOskolkov/database_sql_project.git
```

2. Перейдите в директорию проекта **database_sql_project**;

```
cd database_sql_project
```
3. Подключитесь с PostgreSQL
Можно через pgAdmin или через терминал
4. Создайте базу данных c названием **Northwind_Traders** от пользователя **postgres**
```
CREATE DATABASE Northwind_Traders;
```
5. Перейдите в базу данных **Northwind_Traders**
6. Скопируйте, вставьте и запустите скрипт для наполнения базы данными из файла **"fill_db.sql"**
7. Скопируйте, вставьте и запустите скрипт для создания таблицы **suppliers** из файла **"create_table_suppliers.sql"**
8. Запустите файл **"script_suppliers.py"** для заполнения таблицы **suppliers** данными из файла **"suppliers.json"**
9. Копируйте, вставляйте и запускайте скрипты из файлов с названием **"_page.sql"** для работы с базой данных **Northwind_Traders**


