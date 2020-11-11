from bottle import route, run, template


@route('/')
def index():
    return ('<h1>Hello</h1>')


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080, debug = True)
