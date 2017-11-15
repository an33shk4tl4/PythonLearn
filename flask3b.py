# example input from the URL
#/echo/?&thing=ball&place=willberg

from flask import Flask, render_template, Request

app = Flask(__name__,static_folder='.', static_url_path='/')

@app.route('/echo/')
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html', thing=thing, place=place)


app.run(port=9999, debug=True)
