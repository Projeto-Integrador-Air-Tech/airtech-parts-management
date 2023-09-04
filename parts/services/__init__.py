from flask import Flask
from services.parts_manipulation import PartsManipulation

def run_app():
    parts_app = Flask(__name__)
    PartsManipulation(parts_app)
    return parts_app