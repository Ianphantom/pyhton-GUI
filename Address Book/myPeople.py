from tkinter import *
import sqlite3
import addPeople

con =sqlite3.connect('database.db')
cur =con.cursor()  

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My People")
        self.resizable(False, False)

        ### Frames ###
        self.top=Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame=Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        ### Heading ###
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text="My People", font="arial 15 bold", fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        ### ScrollBar###
        self.sb=Scrollbar(self.bottomFrame, orient=VERTICAL)

        ###listbox###
        self.listBox=Listbox(self.bottomFrame, width=60, height=31)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.sb.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)
        count=0
        persons=cur.execute("SELECT * FROM persons").fetchall()
        for person in persons:
            self.listBox.insert(count, str(person[0])+"-"+str(person[1]))
            count+=1

        ### Buttons ###
        btnadd = Button(self.bottomFrame, text="Add", width=12, font='Sans 12 bold', command=self.funcAddPeople)
        btnadd.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        btnUpdate = Button(self.bottomFrame, text="Update", width=12, font='Sans 12 bold', command=self.funcUpdatePerson)
        btnUpdate.grid(row=0, column=2, sticky=N, padx=10, pady=50)
        
        btnaDisplay = Button(self.bottomFrame, text="Display", width=12, font='Sans 12 bold')
        btnaDisplay.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btnDelete = Button(self.bottomFrame, text="Delete", width=12, font='Sans 12 bold')
        btnDelete.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def funcAddPeople(self):
        addPage=addPeople.AddPeople()
        self.destroy()
    
    def funcUpdatePerson(self):
        global person_id
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id= person.split("-")[0]
        updatePage=Update()

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Update Person")
        self.resizable(False, False)

        ### Get Person from database ###
        global person_id
        person=cur.execute("SELECT * FROM persons WHERE person_id=?", (person_id,))
        person_info = person.fetchall()
        # print(person_info)
        self.person_id = person_info[0][0]
        self.person_name=person_info[0][1]
        self.person_surname=person_info[0][2]
        self.person_email=person_info[0][3]
        self.person_phone=person_info[0][4]
        self.person_address=person_info[0][5]
