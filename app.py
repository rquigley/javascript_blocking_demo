from flask import Flask, render_template, make_response
from time import sleep
import os
app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/demo/<int:page>')
def demo(page):
  if page < 1 or page > 10:
    return 'This page does not exist', 404

  return render_template('demo{0}.html'.format(page))

@app.route('/js-file/<int:sec>')
@app.route('/js-file', defaults={'sec': 0})
def js_file(sec):
  if sec < 15:
    sleep(sec)

  resp = make_response(render_template('script.js'))
  resp.mimetype = 'application/javascript'
  return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

