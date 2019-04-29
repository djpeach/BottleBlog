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


def get_all_posts():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM posts """)
    return cur.fetchall()


def get_post_by_id(id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM posts WHERE id=(?) """, (id, ))
    return cur.fetchone()


def update_post(id, post):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute(""" UPDATE posts SET title=? WHERE id=? """, (*post, id))
    conn.commit()
