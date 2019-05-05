import tornado.web
import sqlite3
import json
import datetime
from random import *

def _execute(query):
    connection = sqlite3.connect('employee.db')
    cursorobj = connection.cursor()
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
        raise
    connection.close()
    return result
    

def initDatabase():
    query = 'CREATE TABLE IF NOT EXISTS employee (\
            id INTEGER PRIMARY KEY,\
            FIO TEXT,\
            Birthday TEXT,\
            Phone TEXT,\
            Sex INTEGER,\
            Depart TEXT)'
    _execute(query)
    
    query = 'CREATE TABLE IF NOT EXISTS salary (\
            id INTEGER PRIMARY KEY,\
            Employee INTEGER,\
            Summ FLOAT,\
            Date TEXT)'
    _execute(query)

        
class MainHandler(tornado.web.RequestHandler):
    
    def initialize(self, bundle_path):	
        self.bundle_path = bundle_path

    def get(self):	
        self.render('index.html', bundle_path = self.bundle_path)


class BaseHandler(tornado.web.RequestHandler):

    CORS_ORIGIN = '*'
    CORS_METHODS = 'POST, DELETE, PUT, OPTIONS'
    CORS_CREDENTIALS = True
    CORS_HEADERS = 'access-control-allow-origin, authorization, content-type'

    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", self.CORS_ORIGIN)

    def options(self,item_id = None):
        # no body
        self.set_header('Access-Control-Allow-Methods', self.CORS_METHODS)
        self.set_header('Access-Control-Allow-Credentials',
                        "true" if self.CORS_CREDENTIALS else "false")
        self.set_header('Access-Control-Allow-Headers', self.CORS_HEADERS)
        self.set_status(204)
        self.finish()


class PersonalHandler(BaseHandler):

    def get(self, item_id = None):
        if item_id == None:
            query = '''select * from employee'''
        else:
            query = '''select * from employee where id = %s ''' %(item_id)
        rows = _execute(query) 
        data_table = []
        for row in rows:
            ro = {}
            ro["id"] = row[0]
            ro["fio"] = { 'id': row[0], 'fio': row[1] }
            ro["birthday"] = row[2]
            ro["phone"] = row[3]
            ro["sex"] = row[4]
            ro["depart"] = row[5]
            data_table.append(ro)
        self.set_status(200)
        self.json_response(json.dumps(data_table))
        
    def put(self, item_id = None):
        if item_id == None:         
            return self.finish("Invalid key")
        
        data = tornado.escape.json_decode(self.request.body)
        fio = tornado.escape.xhtml_escape(data.get('fio'))
        phone = tornado.escape.xhtml_escape(data.get('phone'))
        sex = int(data.get('sex'))
        depart = tornado.escape.xhtml_escape(data.get("depart"))
        birthday = tornado.escape.xhtml_escape(data.get("birthday"))
        
        query = '''update employee set FIO='%s', Birthday='%s', Phone='%s', 
        Sex=%d, Depart='%s' where id = %s''' %(fio, birthday, phone, sex, depart, item_id)
        _execute(query)

        self.set_status(200)
        
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        fio = tornado.escape.xhtml_escape(data.get('fio'))
        phone = tornado.escape.xhtml_escape(data.get('phone'))
        sex = int(data.get('sex'))
        depart = tornado.escape.xhtml_escape(data.get("depart"))
        birthday = tornado.escape.xhtml_escape(data.get("birthday"))
        
        query = '''insert into employee (FIO, Birthday, Phone, Sex, Depart) 
        values ('%s', '%s', '%s', %d, '%s') ''' %(fio, birthday, phone, sex, depart)
        _execute(query)
        self.set_status(200) 

    def delete(self, item_id = None):
        if item_id == None:
            self.set_status(400)
            return self.finish("Invalid key")
        query = '''delete from employee where id = %s ''' %(item_id)
        _execute(query)

        self.set_status(200)


class SalaryHandler(BaseHandler):
    
    def get(self, item_id=None):
        if item_id == None:
            self.set_status(400)
            return self.finish("Invalid key")
        
        query = '''select date, (Select fio from employee where id = %s) as fio,
        summ from salary where employee = %s ''' %(item_id,item_id)
        rows = _execute(query) 
        data_table = []
        for row in rows:
            ro = {}
            ro["date"] = row[0]
            ro["fio"] = row[1] 
            ro["summ"] = row[2]
            data_table.append(ro)
        self.set_status(200) 
        self.json_response(json.dumps(data_table))

    def post(self):
        data = tornado.escape.json_decode(self.request.body)        

        employee = int(data.get('employee'))
        summ = float(data.get('summ'))
        date = datetime.date.today()
        
        query = '''insert into salary (employee, date, summ) 
        values (%d, '%s',%f) ''' %(employee, date.strftime("%d-%m-%Y"), summ)
        _execute(query)
        self.set_status(200)
