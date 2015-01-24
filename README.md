Machine Learning
================

###Definition

###Overview

##Installation

###Linux Packages

The following packages need to be installed through terminal in Ubuntu:

```
# General Packages:
sudo apt-get install python-pip
sudo pip install Flask
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

Python's [Flask](http://flask.pocoo.org/), is a microframework based on Werkzeug.  Specifically, it is a web framework, which includes, a development server, integrated support for unit testing, RESTful API, and Jinja2 templating. This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/geolocation-web/blob/master/app.py) to be running before accessing the web application.

To ensure the flask server is running, simply execute the following within a dedicated terminal console window:

```
cd /var/www/htmls/geolocation-js/
python app.py
```

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
