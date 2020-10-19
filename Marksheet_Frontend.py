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