from flask import Flask,render_template,request
import mysql.connector as mydb
import os


myconn = mydb.connect(
    host = os.environ.get("DB_HOST","localhost"),
    user= os.environ.get("DB_USER","root"),
    password= os.environ.get("DB_PASSWORD","root"),
    database= os.environ.get("DB_NAME","hello")
)

mycursor = myconn.cursor()
mycursor.execute("create table if not exist world (id int, name varchar(20), lastname varchar(20))")
app = Flask(__name__)



@app.route("/",methods=["POST","GET"])
def hello():
    
    if(request.method=="POST"):
        id = request.form.get("id")
        name = request.form.get("name")
        last = request.form.get("last")
        sql = "insert into world(id,name,lastname) values (%s,%s,%s)"
        values = (id,name,last)
        mycursor.execute(sql,values)
        myconn.commit() 
    return render_template('index.html')
    
@app.route("/hello", )
def hello1():
    id = request.args.get("id")
    name = request.args.get("name")
    last = request.args.get("last")
    dict = {
        "id": id,
        "name": name,
        "last" : last
                }
    return dict

app.run(debug=True,port=5000 , host='0.0.0.0')