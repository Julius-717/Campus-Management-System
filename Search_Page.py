# Campus-Management-System
# import libraries
from tkinter import *
import random
import Marksheet_Backend
import Marksheet_Frontend
import tkinter.messagebox
import os

class Window_1():
    def __init__(self, root):
        self.root = root
        self.root.title("Search Page")
        self.root.geometry('1360x750')
        self.root.config(bg = '#6666ff')

        self.roll = StringVar()
        frame = LabelFrame(self.root, width = 1000, height = 100, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
        frame.grid(row = 1, column = 0, padx = 200, pady = 200)

        label = Label(frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'wheat' )
        label.grid(row = 0, column = 0, padx = 100, pady = 10)

        entry = Entry(frame, font = ('arial',25,'bold'), textvariable = self.roll)
        entry.grid(row = 0, column = 1, padx = 30, pady = 20)