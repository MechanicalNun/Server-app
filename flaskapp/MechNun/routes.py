from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def test1():
  return render_template('merge_style_hoods.html')
 
if __name__ == '__main__':
  app.run(debug=True)