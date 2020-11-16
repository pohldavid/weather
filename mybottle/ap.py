from bottle import route, run, template
from sensors import bme280sensor
import subprocess

@route('/')
def index():
    return template('home')

@route('/current')
def index():
    
    data =  bme280sensor.read()
    return template('current.tpl', data)

@route('/style')
def style():
    
    data =  bme280sensor.read()
    return template('style.tpl', data)

@route('/history/<date>')
def notemplate(date):
    return('<h1>' + 'this page will look up data for ' + date + ' with date in format YYYY-MM-DD' + '</h1>')

@route('/atemplate/<name>')
def atemplate(name):
    return template('<b>Hello {{name}} this page uses a template</b>!', name=name)

@route('/test')
def test():
    return template('test')

@route('/pic')
def takepic():
    subprocess.call('./fakepic.sh')
    return ('<p><img alt="image" src="fakepic.jpg"></p>')

@route('/staticimage')
def staticimage():
    return template('staticimage')

@route('/bulma')
def bulma():
    return template('bulmatemplate')

@route('/navbar')
def navbar():
    return template('navbar')

@route('/nearby')
def nearby():
    return template('nearby')


@route('/history')
def history():
    
    data =  bme280sensor.read()

    subprocess.call('./mvlogprevious.sh')

    with open("last", "w") as outfile:
        outfile.write(str(data) + "\n")

    subprocess.call('./log.sh')    

    return template('current.tpl', data)    



run(host='localhost', port=8080, debug = True, reloader = True)
