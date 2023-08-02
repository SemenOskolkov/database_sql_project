CREATE TABLE suppliers
(
	supplier_id SERIAL PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100),
	contact_title varchar(100),
	country varchar(100),
	region varchar(100),
	postal_code varchar(100),
	city varchar(100),
	address varchar(100),
	phone varchar(100),
	fax varchar(100),
	homepage varchar(100),
	products varchar(200)
)