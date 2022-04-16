
from re import template
from flask import Flask, render_template, request
import pymysql


# Open database connection
#db = pymysql.connect(host="",user="root",password="soni",database="kush" )

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/output', methods=['POST'])
def output():
    user = request.form['username']
    password = request.form['password']
    host = request.form['url']
    cmd = request.form['command']
    return render_template('output.html', content="hi from kaushal {} {} {} {}".format(user, password, host, cmd))

if __name__ == '__main__':
    app.run(debug=True)
#db.close()


    # # prepare a cursor object using cursor() method
    # cursor = db.cursor()
    # # execute SQL query using execute() method.
    # cursor.execute("SELECT * from kk")
    # # Fetch a single row using fetchone() method.
    # data = cursor.fetchall()
    # # disconnect from server