
import pymysql.cursors

# To connect MySQL database
class DBConnection:
        conn = pymysql.connect(
                host='localhost',
                user='root',
                password="root",
                db='flask_demo',
                port=3308
            )
        cursor = conn.cursor()