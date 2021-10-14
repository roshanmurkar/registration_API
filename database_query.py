from utility import DBConnection
connection = DBConnection

class DBQuery:
    @staticmethod
    def select_all():
        connection.cursor.execute("select * from login_details")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def insert_data(uname, password):
        connection.cursor.execute("INSERT INTO login_details(name,password)VALUES(%s,%s)", (uname, password))
        connection.conn.commit()
        return True

    @staticmethod
    def delete_data(uname):
        connection.cursor.execute("DELETE FROM login_details WHERE (name) = (%s)", uname)
        connection.conn.commit()
        return True
