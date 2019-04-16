import subprocess
import os
import time
import sys
import sqlite3

IP = "http://wsa27080:5000/"

def data_db(array, flag, result, ochered):
    PATH_BASE = str(sys.path[0]) + '\\base.db'
    print(PATH_BASE)
    con = sqlite3.connect(PATH_BASE)
    cur = con.cursor()
    try:
        cur.execute("DELETE  FROM input")
        con.commit()

        for name,schet in array:
            cur.execute("INSERT INTO input (Name, Coin, flag, result , ochered) VALUES ('{}', {}, {}, {}, {})".format(str(name),schet,flag, result, ochered))
    except Exception:
        print(sys.exc_info())
    else:
        con.commit()
        cur.close()
        con.close()
        return 1

class open_webbrowser(object):
    def __init__(self, array = None, flags = None, result = None, ochered=None):
        self.array, self.flags, self.result, self.ochered = array, flags, result, ochered
        super(open_webbrowser, self).__init__()
    def webOpenUrl(self):
        flag = data_db(self.array , self.flags, self.result , self.ochered)
        if flag == 1:
            subprocess.Popen(r'"' + os.environ["PROGRAMFILES"] + '\Internet Explorer\IEXPLORE.EXE" ' + IP)

    def closeWeb(self):
        os.system("taskkill /im IEXPLORE.EXE")



"""
IEstart.py - Файл управления 
MainWeb.py - Файд сервера его необходимо настроить и запустить первым


open_webbrowser.webOpenUrl():
    Info : Используеться для запуска браузера с передачей пораметров

    array = Спользуеться для передачи имяни человека 
    tabNum = Табельный номер
    flags = Указывает какой HTML запустить   результаты   (передать 0 ),  инструкции (передать 1)
    result = Результат человека
    ochered = Запросили если в  очереди нету человека флаг 0 если есть передать 1

open_webbrowser().closeWeb() 

            Закрывает браузер.
            
            

IP не забываем указать ip-адресс машины на которой запускаете можно по дефолту выставить 127.0.0.1 и порт 5000    
"""


array = [["Женя", "1000"],]
open_webbrowser(array = array,  flags= 1, result= 12543, ochered= 0).webOpenUrl()
time.sleep(1500)
open_webbrowser().closeWeb()


