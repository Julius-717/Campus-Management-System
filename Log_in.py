# Campus-Management-System
from tkinter import *
import tkinter.messagebox
import os
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1350x750')
        self.root.config(bg='lightskyblue')
        self.Frame = Frame(self.root, bg='lightskyblue')
        self.Frame.pack()


        self.Username = StringVar()
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Menu', font = ('arial',55,'bold'), bg = 'lightskyblue', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)