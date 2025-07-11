from .dbInit import dbInit
import os
import sqlite3


conn = None
dbPath = "./orchid.db"


def dbConn():
    global conn
    if conn is None:
        try:
            dbExists = os.path.exists(dbPath)
            conn = sqlite3.connect(dbPath, check_same_thread=False)
            if not dbExists:
                dbInit(conn)
        except sqlite3.Error as e:
            print(f"DB 연결 오류: {e}")
            conn = None
    return conn
