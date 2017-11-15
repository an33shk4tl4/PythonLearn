from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.') 
    # return "It isn't fancy, but it's my home page"

@route('/echo/<name>')
def echo(name):
    return "Hello " + name

run(host='localhost',port=9999, reloader=True)
