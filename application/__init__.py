import logging

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from application import views