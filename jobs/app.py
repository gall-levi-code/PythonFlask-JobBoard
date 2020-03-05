from flask import Flask, render_template, g
import sqlite3

PATH = "db/jobs.sqlite"

app = Flask(__name__)
def open_connection():
    connection = g.__getattr__('_connection')

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')