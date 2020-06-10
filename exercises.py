import pyodbc
from db_connection import MSDBconnection


northwind = MSDBconnection()

def all_entries(query):
    while True:
        row = query.fetchone()
        if row is None:
            break
        print(row)


#1
orders_count = northwind.sql_query("""
SELECT COUNT(*) AS "Total Orders"
FROM Orders""")

print(orders_count.fetchone())

#2
orders_rio = northwind.sql_query("""
SELECT COUNT(*) AS "Total Orders Rio"
FROM Orders
WHERE ShipCity = 'Rio de Janeiro'""")

print(orders_rio.fetchone())

#3
orders_rio_reims = northwind.sql_query("""
SELECT *
FROM Orders
WHERE ShipCity IN ('Rio de Janeiro','Reims')""")

#4
company_name_with_z = northwind.sql_query("""
SELECT *
FROM Customers
WHERE CompanyName LIKE '%[Zz]%'""")

all_entries(company_name_with_z)

#5

