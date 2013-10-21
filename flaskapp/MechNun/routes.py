from flask import Flask, render_template, url_for, jsonify, request
import pygame
import time
import subprocess 
import os
from arduino_nun import *

app = Flask(__name__)      
static = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.route('/')
def test1():
  return render_template('merge_style_hoods.html')
 
@app.route('/name/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    return jsonify(result=a + c * b)

@app.route('/map')
def map():
    
    result= jsonify({
            "Parnassus Heights": {"fillOpacity": 0.9,"fillColor": '#00FF00'},
            "Apparel City": {"fillOpacity": 0.9,"fillColor": '#00FF00'}
            })
    return render_template('merge_style_hoods.html', data = result)


@app.route('/sound')  
def sound():
    song =  '/'.join([static,'Jennifer.mp3'])
    # TODO: initialize the mixer at startup as a class object
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    return 'Playing %s' % song
    

@app.route('/rainbow/') 
@app.route('/rainbow/<int:l>')
def rainbow(l=30):
    leds = [hsv2rgb((360.0 / float(l)) * float(i), 1, 0.5) for i in xrange(l)]
    s.write(command_leds(leds))
    return ''    


@app.route('/index')
def index():
    return render_template('index.html')    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
