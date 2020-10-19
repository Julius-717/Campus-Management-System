# Campus-Management-System
# Import libraries
from tkinter import *
import Marksheet_Backend
import random
import tkinter.messagebox
from tkinter import ttk

def marksheet():
    root = Tk()
    root.title('Marksheet')
    root.geometry('1350x750')
    root.config(bg = 'Navajo white')

    # Variables
    name = StringVar()
    roll = StringVar()
    fname = StringVar()
    mname = StringVar()
    DOB = StringVar()
    gender = StringVar()
    scl = StringVar()
    email = StringVar()
    m1 = DoubleVar()
    m2 = DoubleVar()
    m3 = DoubleVar()
    m4 = DoubleVar()
    m5 = DoubleVar()
    gt = DoubleVar()
    per = DoubleVar()
    cgpa = DoubleVar()
    grade = StringVar()
    div = StringVar()
    result = StringVar()

    # Functions
    def Add():
        if(len(roll.get()) != 0):
            Marksheet_Backend.insert(name.get(),roll.get(),fname.get(),mname.get(),DOB.get(),gender.get(), \
                scl.get(),email.get(),m1.get(),m2.get(),m3.get(),m4.get(),m5.get(), \
                    gt.get(),per.get(),cgpa.get(),grade.get(),div.get(),result.get())