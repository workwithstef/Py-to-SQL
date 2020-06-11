from db_connection import MSDBconnection


class ProductTable(MSDBconnection):

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(id)).fetchone()

    def get_by_name(self, name):
        name_result_table = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{name}%'")
        if name_result_table.fetchone() is None:
            print(f'No results matching "{name}".')
        while True:
            one_entry = name_result_table.fetchone()
            if one_entry is None:
                break
            print(one_entry)

    def get_all(self):
        all_results_table = self.sql_query('SELECT * FROM Products')
        while True:
            one_entry = all_results_table.fetchone()
            if one_entry is None:
                break
            print(one_entry)

    def add_row(self, product_name, product_price, product_stock_level):
        # I WANT TO INSERT VALUES TO THE PRODUCT TABLE CORRESPONDING TO THE CURRENT COLUMNS
        return self.sql_query(f"""
        INSERT INTO Products
        (ProductName, UnitPrice, UnitsInStock)
        VALUES
        ('{product_name}', '{product_price}', '{product_stock_level}')""")

    def add_column(self, column_name):
        self.sql_query(f"""
        ALTER TABLE Products
        ADD COLUMN {column_name}""")


p_table = ProductTable()

# p_table.add_row("Stefans Special Fried Chicken", 10, 25)

p_table.get_by_name('chef')

