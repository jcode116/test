from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Azure! This is the fixed version with Solace Packages'
