import os

from bottle import route, run, template
from bottle import get, post, request, response# or route
from bottle import static_file

#bottle 汉语译为花瓶


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@post('/login/<name>') # or @route('/login', method='POST')
def login(name):
    username = request.forms.get('username')
    password = request.forms.get('password')
    print('username=', username, 'password', password)
    return template('<b>欢迎登陆{{name}}</b>!', name=name)


@route('/static/<filepath:path>')
def server_static(filepath):
    root = "/home/wanghao/PycharmProjects/pyCommon/html"
    root = os.path.abspath(root) + os.sep
    print(root)
    filename = os.path.abspath(os.path.join(root, filepath.strip('/\\')))
    print(filename)
    response.content_type = 'text/html; charset=utf-8'
    response.charset = 'utf-8'
    return static_file(filepath,  root='/home/wanghao/PycharmProjects/pyCommon/html')


run(host='localhost', port=8080, debug=True)

