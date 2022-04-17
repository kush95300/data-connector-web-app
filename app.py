
from re import template
from click import command
from flask import Flask, render_template, request
import pymysql


# Open database connection
class Db:
    def __init__(self):
        print("DB object created")  

    def set(self,user,passwd,host):
        self.user = user
        self.passwd = passwd
        self.host = host       

   
    def connect(self):
        self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd)
        return self.db

    def command(self,cmd):
        con = self.connect()
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
        return cur.fetchall()

    def exit(self):
        self.db.close()

app = Flask(__name__)

db = Db()

@app.route('/')
@app.route('/index')
def index():
    try: db.exit()
    except: print("No connection to close")
    return render_template('index.html')


@app.route('/output', methods=['POST'])
def output():
    user = request.form['username']
    password = request.form['password']
    host = request.form['url']
    db.set(user,password,host)
    return render_template('output.html', content="Enter Command to proceed")

@app.route('/result', methods=['POST'])
def result():
    command = request.form['command']
    data = db.command(command)
    return render_template('output.html', content="Output \n\n\n {}".format(data))


if __name__ == '__main__':
    app.run(debug=True)
