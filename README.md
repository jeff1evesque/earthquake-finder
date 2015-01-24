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

####GIT Submodule

###jQuery Validation

###JSON Schema
