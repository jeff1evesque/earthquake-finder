## @app.py
#  This file loads corresponding logic, and html template file(s), which
#    allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request
from package.json_scraper import scrape

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/json_scraper/', methods=['POST', 'GET'])
def json_scraper():
  if request.method == 'POST':
    return scrape(request.form['gps_dataset'])

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
    debug=True
  )
