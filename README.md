# InspectX Webapp

**Webapp built with Flask, Bootstrap, and deployed on Google App Engine**

**[Live website](https://www.inspect-x.com/)**

## Requirements
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
- 


## Installation

Clone or download this repository

    $ git clone https://github.com/VictorFateh/inspectx-app
    $ cd inspectx-app

Create and activate virtualenv

    $ virtualenv env 
    $ source env/bin/activate

Install dependencies

    $ pip install -r requirements.txt

Run and test the app through the standard GAE environment

	$ dev_appserver.py app.yaml

To see your application, access this url in your browser: 

	http://localhost:8080
	

## Help
[Google Cloud Flask Docs](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)

[Flask Quickstart Docs](http://flask.pocoo.org/docs/1.0/quickstart/)