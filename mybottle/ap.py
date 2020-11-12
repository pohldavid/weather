from bottle import route, run, template
from sensors import bme280
import subprocess

@route('/')
def index():
    
    data =  bme280.read()
    return template('current.tpl', data)

@route('/notemplate/<name>')
def notemplate(name):
    return('<h1>' + name + ' this page is html with no template</h1>')

@route('/atemplate/<name>')
def atemplate(name):
    return template('<b>Hello {{name}} this page uses a template</b>!', name=name)

@route('/test')
def test():
    return template('test')

@route('/pic')
def takepic():
    subprocess.call('./fakepic.sh')

    
    return("just a second - i took a picture")





run(host='localhost', port=8080, debug = True, reloader = True)
