from flask import Flask, render_template
# '''
# passing params via URL
# '''
app = Flask(__name__, static_folder='.', static_url_path='/')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>-<place>')
def echo(thing, place):
    ''' the URL pattern can be anything , meaning a hyphen instead of / between the two
    parameters'''
    return render_template('flask3.html', thing=thing, place=place)


app.run(port=9999, debug=True)
