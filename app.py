# Create a simple flask app
import os
from flask import Flask, render_template
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('index.htm')

@app.route('/about')
def hello_world_about():
    return render_template('about.html')

@app.route('/edu')
def hello_world_edu():
    return render_template('edu.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
