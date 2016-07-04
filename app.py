import os
from flask import Flask, render_template, request, redirect, url_for
from telnetlib import Telnet

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/turn_on', methods = ['GET'])
def turn_on():
    print "Turning on!"
    tel = Telnet('foxnegro.zapto.org')
    tel.write(b'X\n')
    tel.close()
    return render_template('home.html')

@app.route('/turn_off', methods = ['GET'])
def turn_off():
    print "Turning off!"
    tel = Telnet('foxnegro.zapto.org')
    tel.write(b'Y\n')
    tel.close()
    return render_template('home.html')

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
