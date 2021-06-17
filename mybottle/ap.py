from bottle import route, run, template, static_file, request
from sensors import temperature_pressure_humidity
# import subprocess


@route('/')
def index():
    return template('home')


@route('/current')
def index():

    data = temperature_pressure_humidity.read()
    return template('current.tpl', data)


@route('/style')
def style():

    data = temperature_pressure_humidity.read()
    return template('style.tpl', data)


@route('/atemplate/<name>')
def atemplate(name):
    return template('<b>Hello {{name}} this page uses a template</b>!', name=name)


@route('/pic')
def takepic():
    return ('<p><img alt="image" src="/home/pi/weather/mybottle/pic.jpg"></p>')


def latest_pic():
    import glob
    import os

    # * means all if need specific format then *.csv
    list_of_files = glob.glob('/home/pi/weather/stills/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


@route('/latest')
def lastpic():
    return('<h1> ' + latest_pic() + ' </h1>')


@route('/staticimage/<filename>')
def staticimage(filename):
    return static_file(filename, root='/home/pi/weather/stills/', mimetype='image/jpg')


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

    data = temperature_pressure_humidity.read()

    return template('history.tpl', data)


@route('/form')
def index():
    """Home Page"""

    return template("form.tpl", message="Please enter your name")


@route('/form', method="POST")
def formhandler():
    """Handle the form submission"""

    first = request.forms.get('first')
    last = request.forms.get('last')

    message = "Hello " + first + " " + last + "."

    return template("form.tpl", message=message)


run(host='0.0.0.0', port=8080, debug=True, reloader=True)
