# Campus-Management-System
# import library
from tkinter import *
import tkinter.messagebox
import random
import Std_info_Backend
from tkinter import ttk

class Std_info():
    def __init__(self, root):
        self.root = root
        self.root.title('Student Information')
        self.root.geometry('1350x750')
        self.root.config(bg = 'navajowhite')