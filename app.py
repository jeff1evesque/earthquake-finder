## @app.py
#  This file loads corresponding logic, and html template file(s), which
#    allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request
from package.json_scraper import scrape
from package.dataset_iterator import Data_Iterator

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/json_scraper/', methods=['POST', 'GET'])
def json_scraper():
  if request.method == 'POST':
    # get dataset from external webpage
    dataset = scrape(request.form['gps_dataset'])

    # parse dataset for target(s) within specified parameters
    target = Data_Iterator( dataset, request.form['gps_longitude'], request.form['gps_latitude'], request.form['gps_radius'], request.form['daysBack'] )
    target.iterator()
    target_return = target.get_target()

    # return result(s) to browser

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
    debug=True
  )
