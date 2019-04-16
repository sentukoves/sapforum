
import sqlite3
import sys

def data_db():
    PATH_BASE = str(sys.path[0]) + '\\base.db'
    print(PATH_BASE)
    con = sqlite3.connect(PATH_BASE)
    cur = con.cursor()
    try:
        cur.execute("*")
    except Exception:
        print(sys.exc_info())
    else:
        con.commit()
        cur.close()
        con.close()
data_db()