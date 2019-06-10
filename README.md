# Cloudant DB Client
A Python wrapper to simplify Cloudant DB search.

* [Installation](#installation)
* [Usage](#usage)
* [Unittests](#unittests)

## Installation
The wrapper uses base Python3.x libraries and the Cloudant Python Client only.

I suggest to use [virtualenv](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) with Python 3.x.
After installing virtualenv create it:

`mkdir ~/cloudantdbclient`

`virtualenv ~/cloudantdbclient/venv`

Activate the env.:

`cd ~/cloudantdbclient`

`source venv/bin/activate`

Checkout the source:

`git clone https://github.com/istvanbolya/cloudant_client.git`

Install packages:

`pip install -r cloudant_client/requirements.txt`
    
 ## Usage
 You can find a sample script `use_client.py` how can you interact with the client and also which parameters are needed.
 
 `python cloudant_client/use_client.py`
 
 ## Unittests
 You can run the unittests by executing the script under virtualenv:
 
 `python cloudant_client/client/tests.py`
