# Campus-Management-System
# import database
import sqlite3

def connect():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
        address text, mobno integer,email text, dob integer, gender text)")

    conn.commit()
    conn.close()