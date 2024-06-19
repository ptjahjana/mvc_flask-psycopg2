
import os
import psycopg2

class BaseController:
    def get_db_connection():
        conn = psycopg2.connect(host='localhost',
                                database='flask_db',
            user="root",
            password="12345678")
        return conn