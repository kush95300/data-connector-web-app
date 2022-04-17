from re import template
from click import command
from flask import Flask, render_template, request
import pymysql
# Open database connection
class Db:
    def __init__(self):
        print("DB object created")  
    def set(self,user,passwd,host,dbs):
        self.user = user
        self.passwd = passwd
        self.host = host   
        self.dbs = dbs    
   
    def connect(self):
        if self.dbs is None or self.dbs == "":
            self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd)       
        else:
            self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbs)
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
user = "user"
host = "hoast"
passwd = "pass"
database = ""
db = Db()
@app.route('/')
@app.route('/index')
def index():
    try: db.exit()
    except: print("No connection to close")
    return render_template('index.html')
@app.route('/output', methods=['POST'])
def output():
    global user
    global passwd
    global host
    global database
    print( user, passwd,host,database)
    user = request.form['username']
    passwd = request.form['password']
    host = request.form['url']
    database = request.form['database']
    print( user, passwd,host,database)
    db.set(user,passwd,host,database)
    return render_template('output.html', content="Enter Command to proceed")
@app.route('/result', methods=['POST'])
def result():
    global user
    global passwd
    global host
    command = request.form['command']
    print( user, passwd,host,database)
    data = db.command(command)
    return render_template('output.html', content="Output \n\n\n {}".format(data))
if __name__ == '__main__':
    app.run(debug=True)