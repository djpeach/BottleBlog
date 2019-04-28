from bottle import run
from routes import domain, blog


run(host='localhost', port=8080, debug=True, reloader=True)