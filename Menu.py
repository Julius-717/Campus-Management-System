# Campus-Management-System
# import libraries
from tkinter import *
import random
import os

def __marksheet__():
   filename = 'Search_Page.py'
   os.system(filename)
   os.system('vscode'+filename)

def __Library__():
    filename = 'Library_Frontend.py'
    os.system(filename)
    os.system('vscode'+filename)

def __Information__():
    filename = 'Std_info_Frontend.py'
    os.system(filename)
    os.system('vscode'+filename)

def __FeeReport__():
    filename = 'Fee_Frontend.py'
    os.system(filename)
    os.system('vscode'+filename)

def menu():
    root = Tk()
    root.title('Menu')
    root.geometry('1350x750')
    root.config(bg='navajo white')

    title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
    title_Frame.grid(row = 0, column = 0, pady = 50)
       
    title_Label = Label(title_Frame, text = 'MENU', font = ('arial',30,'bold'), bg = 'navajo white')
    title_Label.grid(row = 0, column = 0, padx = 150)

    # Frame5
    Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
    Frame_1.grid(row = 1, column = 0, padx = 280)
    Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
    Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
    Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
    Frame_3.grid(row = 3, column = 0, pady = 7)
    Frame_4 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
    Frame_4.grid(row = 4, column = 0, pady = 7)