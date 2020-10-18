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

            def Add():
                if(len(self.name.get()) != 0):
                    Std_info_Backend.insert(self.name.get(), self.fname.get(), self.surname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                        self.gender.get())
                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (self.name.get(), self.fname.get(), self.surname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                        self.gender.get()))

            def display():
                self.listbox.delete(0, END)
                for row in Std_info_Backend.view():
                    self.listbox.insert(END, row, str(' '))

            def Exit():
                Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if Exit > 0:
                    self.master.destroy()
                    return 

            def Reset():
                self.name.set('')
                self.fname.set('')
                self.surname.set('')
                self.address.set('')                        self.mobno.set('')
                self.email.set('')
                self.dob.set('')
                self.gender.set('')
                self.listbox.delete(0, END)

            def Delete():
                if(len(self.name.get()) !=0):
                    Std_info_Backend.delete(selected_tuple[0])
                    Reset()
                    Display()

            def Search():
                self.listbox.delete(0, END)
                for row in Std_info_Backend.search(self.name.get(), self.fname.get(), self.surname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), self.gender.get()):
                    self.listbox.insert(END, row, str(''))

            def Update():
                if(len(self.name.get()) != 0):
                    Std_info_Backend.delete(selected_tuple[0])
                if(len(self.name.get()) != 0):
                    Std_info_Backend.insert(self.name.get(), self.fname.get(), self.surname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                        self.gender.get())

                    Std_info_Backend.insert(self.name.get(), self.fname.get(), self.surname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                        self.gender.get())

            # Frames
            self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'navajowhite',bd = 15, relief = 'ridge')
            self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT INFORMATION ')
            self.Frame_1.grid(row = 1, column = 0, padx = 10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT DATABASE')
            self.Frame_2.grid(row = 1, column = 1, padx = 5)                  
    
            self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                   bg = 'navajowhite', relief = 'ridge', bd = 13)
            self.Frame_3.grid(row = 2, column = 0, pady = 10)
