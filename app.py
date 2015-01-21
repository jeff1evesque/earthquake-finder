## @app.py
#  This file loads corresponding logic, and html template file(s), which
#    allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request, jsonify

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
    debug=True
  )
