# Python-to-SQL 

## This repo contains all things pyodbc related

### Procedure to connect Pycharm with SQL database:
- First step is to 'import pyodbc'
- Next enter the following string, and save it to a variable
```
connect_python = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+
                                'DATABASE='+database+';UID='+username+';PWD='+password)
```
(Inputs; server, database, username & password, are all obtained from SQL Server you wish to link)
- Define the cursor which you will use to enter SQL commands in Pycharm, using the .cursor() method 
(usually saved to variable name 'cursor')
```
cursor = connect_python.cursor()
```
- Use .execute method to execute SQL commands; they should be input as an argument in string-format
```
customers = cursor.execute('SELECT * FROM Customers')
```
- Successfully run an SQL command in Pycharm!

### Handling SQL received data

- .fetchone() - fetches one entry of received data
- .fetchall() - fetches all entries of received data
- .fetchmany(num) - fetches specific num of received data
 
##### REMEMBER: cursor remains state -- meaning the data is like a stack of cards,
          if you take (fetch) one, it removes it from the stack

- customers.fetchone() - will return a pyodbc Row object filled with data
- Method to efficiently loop through all rows in Customers table
```
while True:
    row = customers.fetchone()
    print(row)
    if row is None:
        break
```