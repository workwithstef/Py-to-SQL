from db_connection import MSDBconnection


class ProductTable(MSDBconnection):

    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(id)).fetchone()

    def get_all(self):
        results_list = []
        row = self.sql_query('SELECT * FROM Products').fetchone()
        while True:
            if row is None:
                break
            results_list.append(row)
        return results_list


p_table = ProductTable()

print(p_table.get_by_id(3))
