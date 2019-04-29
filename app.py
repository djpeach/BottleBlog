from bottle import run
from routes import domain, blog
from data.database import create_table

posts_table_creation = """ CREATE TABLE IF NOT EXISTS posts (
        id integer PRIMARY KEY,
        title text NOT NULL
        ); """

create_table(posts_table_creation)


run(host='localhost', port=8080, debug=True, reloader=True)