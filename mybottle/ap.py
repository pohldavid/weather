from bottle import route, run, template

import subprocess

@route('/')
def index():
    content =  {'date':'tehdate', 'time':'tehtime', 'temp':'thetemp','press':'thepress','humidity':'thehumid'}
    return template('current.tpl', content)

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
