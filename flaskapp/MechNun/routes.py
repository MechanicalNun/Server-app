from flask import Flask, render_template, url_for, jsonify, request
import time
import subprocess 
import os

app = Flask(__name__)      
 
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
    # song =  '/Users/Oren/Music/Kalya Scintilla/Kalya Scintilla Bluetech - 667 (Kalya Scintilla Remix).mp3'

    static = '/Users/Oren/Coding/MechanicalNun/Server-app/flaskapp/MechNun/static'
    song =  '/'.join([static,'Animals.m4a'])
    player = subprocess.Popen(['mplayer', song, '-ss', "30"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)  
    time.sleep(4)
    player.stdin.write("q")
    # out = ', '.join(os.listdir(str(os.getcwd())))
    # out = ', '.join(os.listdir(str("/Users/Oren/Coding/MechanicalNun/Server-app/flaskapp/MechNun/static")))
    out = song
    return out
    


@app.route('/index')
def index():
    return render_template('index.html')    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
