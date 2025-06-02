from dbConn import dbConn
import atexit


def dbClose():
    conn = dbConn()
    if conn:
        conn.close()
        conn = None


atexit.register(dbClose)
