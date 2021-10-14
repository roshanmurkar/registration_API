
import psycopg2.extras
# import pymysql.cursors
import os
from dotenv import load_dotenv



from dotenv import dotenv_values

config = dotenv_values(".env")

print(config)
load_dotenv()

class DBConnection:
    conn = psycopg2.connect(
        host=config.get('HOST'),
        database=config.get('DATABASE'),
        user=config.get('USER'),
        password=config.get('PASSWORD'),
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    cursor = conn.cursor()

#
# class DBConnection:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="flask_demo",
#         user="postgres",
#         password="root",
#         cursor_factory=psycopg2.extras.RealDictCursor
#     )
#     cursor = conn.cursor()


# To connect MySQL database
# class DBConnection:
#         conn = pymysql.connect(
#                 host='localhost',
#                 user='root',
#                 password="root",
#                 db='flask_demo',
#                 port=3308,
#                 cursorclass=pymysql.cursors.DictCursor
#             )
#         cursor = conn.cursor()