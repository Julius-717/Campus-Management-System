# Campus-Management-System
# Import libraries
from tkinter import *
import sqlite3

def connect():
    con = sqlite3.connect('Marks.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Marks (id INTEGER PRIMARY KEY, name text, roll integer, fname text, mname \
        text, DOB integer, gender text, scl text, email text, m1 integer, m2 integer, m3 integer, m4 integer, \
            m5 integer, gt integer, per integer, cgpa integer, grade text, div text, result text)')

    con.commit()
    con.close()