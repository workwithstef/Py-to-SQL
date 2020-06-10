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