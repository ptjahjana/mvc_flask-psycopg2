from flask import Flask, render_template
import psycopg2
from base_controller import BaseController

class BooksController(BaseController):
    def index():
        conn = BaseController.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM books;')
        books = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('books/index.html', books=books)


b