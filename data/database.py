import sqlite3

conn = None
c = None


def create_connection():
    global conn, c
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()


def create_table(sql):
    global c
    c.execute(sql)
