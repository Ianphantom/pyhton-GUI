from tkinter import *
import datetime
import myPeople
import addPeople
import aboutUs

date = datetime.datetime.now().date()

class Application(object):
    def __init__(self, master):
        self.master = master

        ### Frames ###
        self.top=Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom=Frame(master, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        ### Heading ###
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text="My Address Book", font="arial 15 bold", fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)
        self.date_lbl=Label(self.top, text='Today\'s date' + str(date), font='arial 12 bold', bg='White', fg='#ffa500')
        self.date_lbl.place(x=450, y=5)

        ### Buttons ###
        self.btn1_icon=PhotoImage(file='icons/man.png')
        self.personBtn=Button(self.bottom, text='  My People', font="arial 12 bold", width=150, command=self.openMyPeople)
        self.personBtn.config(image=self.btn1_icon, compound=LEFT)
        self.personBtn.place(x=250, y=10)

        self.btn2_icon=PhotoImage(file='icons/add.png')
        self.addPersonBtn=Button(self.bottom, text='  Add People', font="arial 12 bold", width=150, command=self.funcAddPeople)
        self.addPersonBtn.config(image=self.btn2_icon, compound=LEFT)
        self.addPersonBtn.place(x=250, y=70)

        self.btn3_icon=PhotoImage(file='icons/info.png')
        self.aboutBtn=Button(self.bottom, text='  About Us', font="arial 12 bold", width=150, command=aboutUs.main)
        self.aboutBtn.config(image=self.btn3_icon, compound=LEFT)
        self.aboutBtn.place(x=250, y=130)

    def openMyPeople(self):
        people=myPeople.MyPeople()

    def funcAddPeople(self):
        addPerson= addPeople.AddPeople()
        

def main():
    root = Tk() 
    app = Application(root)
    root.title("Address Book App")
    root.geometry("650x400+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()