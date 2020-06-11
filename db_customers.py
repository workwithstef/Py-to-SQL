from db_connection import MSDBconnection


class Customers(MSDBconnection):

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE CustomerID=' + str(id)).fetchone()

    def get_by_company(self, company_name):
        name_result = self.sql_query(f"SELECT * FROM Products WHERE CompanyName LIKE '%{company_name}%'").fetchone()
        if name_result is None:
            return f'No results matching {company_name}.'
        else:
            return name_result

    def get_by_city(self, city):
        city_result = self.sql_query(f"SELECT * FROM Products WHERE City LIKE '%{city}%'").fetchone()
        if city_result is None:
            return f'No results matching {city_result}.'
        else:
            return city_result

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




