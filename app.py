from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('index.html')

@app.route('/certifications')
def certifications():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
