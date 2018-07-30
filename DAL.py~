# -*- coding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf-8')




class Mysql(object):
    """
    Mysql 连接
    """

    def __init__(self, ip, port, user, pwd, database, charset="utf8", autocommit=1):
        import MySQLdb
        connjson = {}
        connjson["host"] = ip
        connjson["port"] = int(port)
        connjson["user"] = user
        connjson["passwd"] = pwd
        connjson["db"] = database
        connjson["charset"] = "utf8"
        self._conn = MySQLdb.connect(**connjson)
        self._conn.autocommit(autocommit)
        self._cursor = self._conn.cursor()

    def execute(self, sql):
        self._cursor.execute(sql)
        return self._cursor.rowcount, self._cursor.fetchall()

    def commit(self):
        self._conn.commit()

    def close(self):
        self._cursor.close
        self._conn.close()



