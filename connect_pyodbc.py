import pyodbc

server = 'databases2.spartaglobal.academy;'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# connects python to SQL database
connect_python = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+
                                'DATABASE='+database+';UID='+username+';PWD='+password)

# acts as a cursor in SQL
cursor = connect_python.cursor()

# executes SQL command
query_result = cursor.execute('SELECT * FROM Products')
print(type(query_result))

# REMEMBER: cursor remains state -- meaning the data is like a stack of cards,
#           if you take (fetch) one, it removes it from the stack.

# fetchone() - fetches one entry in SQL result; removing it from the stack
# result is received as a 'pyodbc.Row' object, which can be interpreted as a list
one_entry = query_result.fetchone()
print(query_result.fetchone())
print(type(one_entry))
# fetchall() - fetches all entries in SQL result

all_results = query_result.fetchall()
# fetchall() results are received as a list
# lists are iterable.
print(type(all_results))

# iterating over fetchall list
#     for data in all_results:
#         print(data.ProductName, data.UnitPrice)

# fetchall == DANGEROUS. Because all data is received as a single list.
# when dealing with very large databases, fetchall() method could jam the server
# Generally, do not use in real life.

customers = cursor.execute('SELECT * FROM Customers')

# continuously loops, re-assigns the fetched result, then prints it, continuously
# until fetched result is None (~till there are no cards left)
# Good way to iterate over database
while True:
    row = customers.fetchone()
    if row is None:
        break
    print(row)


id_price = cursor.execute('SELECT ProductID, UnitPrice FROM Products')
# fetchmany() - used to fetch a specific amount of entries
print(id_price.fetchmany(20))
