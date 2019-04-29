import sqlite3


def create_table(sql):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute(sql)


def add_post(post):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute(""" INSERT INTO posts (title) VALUES (?); """, post)
    conn.commit()
    return cur.lastrowid
