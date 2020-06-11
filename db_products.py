from db_connection import MSDBconnection


class ProductTable(MSDBconnection):

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(id)).fetchone()

    def get_by_name(self, name):
        return self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{name}%'").fetchone()

    def get_all(self):

        while True:
            row = self.sql_query('SELECT * FROM Products').fetchone()
            if row is None:
                break
            print(row)
        # return results_list

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

<<<<<<< HEAD
print(type(p_table.get_by_id(3)))

p_table.add_row("Stefans Special Fried Chicken", 10, 25)
=======
# print(type(p_table.get_by_id(3)))

p_table.add_row("Stefans Special Fried Chicken", 10, 25)

# print(p_table.get_by_name('Stefan'))
p_table.get_all()
>>>>>>> 13fa32d7829a39b8aa732df297dc6a5c50b30c11
