# this files sole purpose is to initialize the app on first start up

# importing flask dependency
from flask import Flask

# initialize and instantiate the flask object
app = Flask(__name__)

# now import the routes module to the newly minted flask object
from rycorp_app import routes
