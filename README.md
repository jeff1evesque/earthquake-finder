Earthquake Finder
================

###Definition

[GeoJSON](http://en.wikipedia.org/wiki/GeoJSON) is an [open standard](http://en.wikipedia.org/wiki/Open_standard) format for encoding [simple geographical features](http://en.wikipedia.org/wiki/Simple_Features).  It specifically uses the [JSON standard](http://www.json.org/).

###Overview

This project provides an HTML [webform](http://en.wikipedia.org/wiki/Form_%28HTML%29), where users supply information such as their [GPS](http://en.wikipedia.org/wiki/Geographic_coordinate_system) coordinates ([longitude](http://en.wikipedia.org/wiki/Longitude), [latitude](http://en.wikipedia.org/wiki/Latitude)), a [geojson](http://en.wikipedia.org/wiki/GeoJSON) formatted [dataset](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson) of earthquake instances, and restriction parameters (radius, days).

When the user submits the webform (via [ajax](http://en.wikipedia.org/wiki/Ajax_%28programming%29)), the server determines the largest magnitude [earthquake](http://en.wikipedia.org/wiki/Earthquake) from the given dataset, relative to the supplied GPS coordinates, with respect to the acceptable radius, and number of days back from today (when webform is submitted).  The determined largest earthquake relative to the parameters supplied, is returned to the [web browser](http://en.wikipedia.org/wiki/Web_browser) (via ajax).

**Note:** for information regarding acceptable geojson structure, refer to the [Request](https://github.com/jeff1evesque/geolocation-web#request) section below.

##Installation

###Linux Packages

The following packages need to be installed through terminal in Ubuntu:

```
# General Packages:
sudo apt-get install python-pip
sudo pip install Flask
sudo pip install requests
sudo pip install jsonschema
```

**Note:** Though, this project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system, any flavor of linux will work.

##Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/html/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/geolocation-web.git
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/www/html/
sudo chown -R jeffrey:sudo geolocation-web
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/html/geolocation-web/
git remote add upstream https://github.com/[YOUR-USERNAME]/geolocation-web.git
```

###Flask

Python's [Flask](http://flask.pocoo.org/), is a microframework based on [Werkzeug](http://werkzeug.pocoo.org/).  Specifically, it is a [web framework](http://en.wikipedia.org/wiki/Web_application_framework), which includes, a development server, integrated support for [unit testing](http://en.wikipedia.org/wiki/Unit_testing), [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API, and [Jinja2](http://jinja.pocoo.org/) templating.

This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/app.py) to be running:

```
cd /var/www/html/geolocation-js/
python app.py
```

**Note:** ensure that the terminal window running the above script, is not used for any other purposes, while the web application is available to others.

####Request

Python's [`Request`](http://docs.python-requests.org/) API, provides an elegant, yet easy implementation for making various [HTTP requests](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods).  This project implements the `get` request to parse the supplied `geojson` [dataset](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson), from a specified external webpage.

The following `request` implementation is made within [`json_scraper.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/package/json_scraper.py):

```
  response = requests.get(url)
  content  = r.json()
```

**Note:** the above `json()` method, decodes the `response` as a json object.

###jQuery Validation

[jQuery Validation](http://jqueryvalidation.org/) is a plugin that allows [client-side](http://en.wikipedia.org/wiki/Client-side) validation on [HTML form](http://www.w3.org/TR/html5/forms.html) elements. When a specific field fails validation, a label element is created as the next successive [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) element, indicating the corresponding *error message*.

Additional documentation:

- [jQuery Validation](http://jqueryvalidation.org/documentation/)
- [Validator object](http://jqueryvalidation.org/category/validator/)
- [Validator addMethod](http://jqueryvalidation.org/jQuery.validator.addMethod/)
- [Validation example](http://stackoverflow.com/questions/10843399#answer-10843593)

This project implements client-side validation within [`form_validator.js`](https://github.com/jeff1evesque/geolocation-web/blob/master/static/js/form_validator.js). Specific *how-to* can be found within the comments of the javascript [code](https://github.com/jeff1evesque/geolocation-web/blob/master/static/js/form_validator.js).

###JSON Schema

[JSON Schema](https://pypi.python.org/pypi/jsonschema) provides an implementation to validate [JSON](http://en.wikipedia.org/wiki/JSON) data structures. When a specific element within the JSON structure fails validation, an [exception](https://wiki.python.org/moin/HandlingExceptions) is raised indicating the corresponding *error message*.

Additional documentation:

- [Understanding JSON Schema](http://spacetelescope.github.io/understanding-json-schema/)
- [jsonschema](http://python-jsonschema.readthedocs.org/en/latest/)

This project implements *JSON Schema* validation, as a backend-validation tool. Specifically, [`jsonschema_definitions.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/package/jsonschema_definitions.py) defines acceptable *schemas* to validate against, while [`data_iterator.py`](https://github.com/jeff1evesque/geolocation-web/blob/b6bbc65dae4d9c361ce7daa58a4a670ffac55ff5/package/dataset_iterator.py#L61) implements the validation schema.

###Custom Validation

When the HTML webform of the web-interface is submitted, the server-side receives an array of text elements, corresponding to each form `<input>` element.  To perform meaningful validation on the server-side, each array element is submitted to a respective function within [`validator_functions.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/package/validator_functions.py).  This file attempts to cast variables to their equivalent type, with the exception of the dataset url case.  If casting does not raise an error, variables are checked against their defined bounds.  If any custom validation fails, the corresponding function returns `status: False`.  This prevents the remaining logic of `json_scraper` within [`app.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/app.py) from executing. 
