from db_connection import MSDBconnection


class Customers(MSDBconnection):

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Customers WHERE CustomerID=' + str(id)).fetchone()

    def get_by_company(self, company_name):
        while True:
            name_result = self.sql_query(f"SELECT * FROM Customers WHERE CompanyName LIKE '%[{company_name}]%'").fetchone()
            if name_result is None:
                break
            # if name_result is None:
            #     return f'No results matching {company_name}.'
            else:
                return name_result

    def get_by_city(self, city):
        city_result_table = self.sql_query(f"SELECT * FROM Customers WHERE City = '{city.capitalize()}'")
        if city_result_table.fetchone() is None:
            print(f'No results matching {city}.')
        while True:
            one_entry = city_result_table.fetchone()
            if one_entry is None:
                break
            print(one_entry)

    # def get_all(self):
    #
    #     while True:
    #         row = self.sql_query('SELECT * FROM Products').fetchone()
    #         if row is None:
    #             break
    #         print(row)

    def add_row(self, company_name, city_name, postcode, country):
        return self.sql_query(f"""
            INSERT INTO Customers
            (CompanyName, City, PostalCode, Country)
            VALUES
            ('{company_name}', '{city_name}', '{postcode}', '{country})""")

    def add_column(self, column_name):
        return self.sql_query(f"""
            ALTER TABLE Customers
            ADD COLUMN {column_name}""")


client_table = Customers()

client_table.get_by_city('Lonon')

