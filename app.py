## @app.py
#  This file loads corresponding logic, and html template file(s), which
#    allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request
from package.json_scraper import scrape
from package.dataset_iterator import Data_Iterator
from package.validator_request import validate_request
import json

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/json_scraper/', methods=['POST', 'GET'])
def json_scraper():
  if request.method == 'POST':
    # validate request
    dict_request = { 'longitude': request.form['gps_longitude'], 'latitude': request.form['gps_latitude'], 'radius': request.form['gps_radius'], 'daysBack': request.form['daysBack'] }
    validate(dict_request, jsonschema_request())

    # get dataset from external webpage
    dataset = scrape(request.form['gps_dataset'])

    # parse dataset for target(s) within specified parameters
    target = Data_Iterator( dataset, dict_request )
    target.iterator()
    target_return = target.get_largest_target()

    # return result(s) to browser
    return json.dumps(target_return)

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
    debug=True
  )
