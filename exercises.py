import pyodbc


class MSDBconnection():
    def __init__(self, database='Northwind', server='databases2.spartaglobal.academy', username='SA', password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self.establish_connection()
        self.cursor = self.conn.cursor()

    def establish_connection(self):
        connect = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return connect

    def sql_query(self, sql_string):
        return self.cursor.execute(sql_string)


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

