# Cloudant DB Client
A Python wrapper to simplify Cloudant DB search.

* [Installation](#installation)
* [Usage](#usage)

## Installation
The wrapper uses base Python3.x libraries and the Cloudant Python client only.

I suggest to use [virtualenv](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) with Python 3.x.
After installing virtualenv, checkout the source:

`git clone https://github.com/istvanbolya/cloudant_client.git`

Create virtualenv:

`mkdir ~/cloudantdbclient`

`virtualenv ~/cloudantdbclient/venv`

Activate the env. and install packages:

`cd ~/cloudantdbclient`

`source venv/bin/activate`

`pip install -r cloudant_client/requirements.txt`
    
 ## Usage
 You can find a sample, `use_client.py` how can you use the client and also which parameters are needed.
