from tkinter import *
from tkinter import messagebox
import sqlite3

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False, False)

        ### Top Frames ###
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        ### Botton Frames ###
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        ### Heading ###
        self.top_iamge = PhotoImage(file='icons/addbook.png')
        top_image_lbl = Label(self.topFrame, image=self.top_iamge, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text=' Add book ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ### Name ###
        self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 12 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)

        self.ent_name = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_name.insert(0, 'Please enter a book name')
        self.ent_name.place(x=150, y=40)

        ### Author ###
        self.lbl_author = Label(self.bottomFrame, text='Author :', font='arial 12 bold', fg='white', bg='#fcc324')
        self.lbl_author.place(x=40, y=80)

        self.ent_author = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_author.insert(0, 'Please enter a author name')
        self.ent_author.place(x=150, y=80)

        ### page ###
        self.lbl_page = Label(self.bottomFrame, text='Page :', font='arial 12 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40, y=120)

        self.ent_page = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_page.insert(0, 'Please enter a page name')
        self.ent_page.place(x=150, y=120)

        ### Language ###
        self.lbl_lang = Label(self.bottomFrame, text='Language :', font='arial 12 bold', fg='white', bg='#fcc324')
        self.lbl_lang.place(x=40, y=160)

        self.ent_lang = Entry(self.bottomFrame, width=30, bd=3)
        self.ent_lang.insert(0, 'Please enter a languange name')
        self.ent_lang.place(x=150, y=160)

        ### button ###
        button = Button(self.bottomFrame, text='Add Book', command=self.addBook)
        button.place(x=270, y=200)

    def addBook(self):
        pass

