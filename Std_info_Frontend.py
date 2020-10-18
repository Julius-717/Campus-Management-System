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

        def Information():
            # Variables
            self.name = StringVar()
            self.fname = StringVar()
            self.surname = StringVar()
            self.address = StringVar()
            self.mobno = StringVar()
            self.email = StringVar()
            self.dob = StringVar()
            self.gender = StringVar()

            # Functions
            def StudentRec(event):
                try:
                    global selected_tuple

                    index = self.listbox.curseselection()[0]
                    selected_tuple = self.listbox.get(index)

                    self.Entry_name.delete(0, END)
                    self.Entry_name.insert(END, selected_tuple[1])
                    self.Entry_fname.delete(0, END)
                    self.Entry_fname.insert(END, selected_tuple[2])
                    self.Entry_surname.delete(0, END)
                    self.Entry_surname.insert(END, selected_tuple[3])
                    self.Entry_address.delete(0, END)
                    self.Entry_address.insert(END, selected_tuple[4])
                    self.Entry_mobno.delete(0, END)
                    self.Entry_mobno.insert(END, selected_tuple[5])
                    self.Entry_email.delete(0, END)
                    self.Entry_email.insert(END, selected_tuple[6])
                    self.Entry_dob.delete(0, END)
                    self.Entry_dob.insert(END, selected_tuple[7])
                    self.Entry_gender.delete(0, END)
                    self.Entry_gender.insert(END, selected_tuple[8])
                except IndexError:
                    pass