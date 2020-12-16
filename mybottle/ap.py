from bottle import route, run, template
from sensors import temperature_pressure_humidity
import subprocess

@route('/')
def index():
    return template('home')

@route('/current')
def index():
    
    data =  temperature_pressure_humidity.read()
    return template('current.tpl', data)

@route('/style')
def style():
    
    data =  temperature_pressure_humidity.read()
    return template('style.tpl', data)

@route('/atemplate/<name>')
def atemplate(name):
    return template('<b>Hello {{name}} this page uses a template</b>!', name=name)

@route('/pic')
def takepic():
    subprocess.call('./fakepic.sh')
    return ('<p><img alt="image" src="fakepic.jpg"></p>')

@route('/staticimage')
def staticimage():
    return template('staticimage')

@route('/bulma')
def bulma():
    return template('bulma')

@route('/navbar')
def navbar():
    return template('navbar')

@route('/nearby')
def nearby():
    return template('nearby')

@route('/history')
def history():
    
    data =  temperature_pressure_humidity.read()

    return template('history.tpl', data)    

run(host='0.0.0.0', port=8080, debug = True, reloader = True)
