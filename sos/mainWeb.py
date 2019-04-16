from flask import Flask, render_template, request
import sys
import sqlite3
import datetime
app = Flask(__name__)

def data_db():
    PATH_BASE = str(sys.path[0]) + '\\base.db'
    print(PATH_BASE)
    con = sqlite3.connect(PATH_BASE)
    cur = con.cursor()
    try:
        cur.execute("select Name , Coin , flag,  result , ochered from input where temp = 1")
    except Exception:
        print(sys.exc_info())
    else:
        ret_cur = cur.fetchall()
        cur.close()
        con.close()
        return ret_cur


@app.route("/")
def index():
    if request.method == 'GET':
        Player = data_db()
        flag = data_db()[0][2]
        result = data_db()[0][3]
        ochered = data_db()[0][4]
        return render_template("rules.html" , Player=Player, flag=flag, ochered=ochered, result= result , datetime = str(datetime.datetime.now()))

""" Измени Ip и HOST или выстави по дефолту 127.0.0.1 и порт 5000 """

def start_server():
    app.run(host="wsa27080" ,port=5000, debug=True)

start_server()

