import sqlite3

class DBObj:
    sqlite3_dbname = ""
    db = None
    cursor = None

    def __init__(self):
        self.obj_data = {}
        self.obj_list = []

    def open(self, sqlite3_name):
        self.sqlite3_dbname = sqlite3_name
        self.db = sqlite3.connect(self.sqlite3_dbname)
        self.cursor = self.db.cursor()

    def close(self):
        if self.db != None:
            self.db.close()

    def commit(self):
        self.db.commit()

    def sql_exec(self, sql):
        self.cursor.execute(sql)
        self.commit()
        return self.cursor

    def find(self,Number):
        self.cursor.execute("select * from mark_data where applicationNumber ="+str(Number))
        list = self.cursor.fetchone()
        da ={}
        da['agentname'] =list[1]
        da['applicationname']=list[2]
        da['applicationdate'] = list[3]
        da['applicationnumber'] = list[4]
        da['applicationstatus'] = list[5]
        da['bigdraw'] = list[6]
        da['classiificationcode'] = list[7]
        da['draw'] = list[8]
        da['title'] = list[10]
        da['viennacode'] = list[11]
        return da