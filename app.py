from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

# DO NOT run app.run() manually
# Gunicorn will run the app
