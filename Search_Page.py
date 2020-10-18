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