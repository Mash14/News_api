from app.config import DevConfig
from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config = True)

# Setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config')

from app import views