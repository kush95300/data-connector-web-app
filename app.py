
from re import template
from click import command
from flask import Flask, render_template, request
import pymysql


# Open database connection

db = ""

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    try: db.close()
    except: print("No connection to close")
    return render_template('index.html')


@app.route('/output', methods=['POST'])
def output():
    user = request.form['username']
    password = request.form['password']
    host = request.form['url']
    #cmd = request.form['command']
    global db
    db = pymysql.connect(host=host,user=user,password=password )
    return render_template('output.html', content="Enter Command to proceed")

@app.route('/result', methods=['POST'])
def result():
    command = request.form['command']
    #cmd = request.form['command']
    # db = pymysql.connect(host=host,user=user,password=password )
    # # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # # execute SQL query using execute() method.
    cursor.execute(command)
    # # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    return render_template('output.html', content="hi {}".format(data))


if __name__ == '__main__':
    app.run(debug=True)
