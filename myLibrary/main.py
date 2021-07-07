from tkinter import *
from tkinter import ttk
import sqlite3
import addBook

con = sqlite3.connect('library.db')
cur = con.cursor()

class Main(object):
    def __init__(self, master):
        self.master = master

        ### frames ###

        mainFrame = Frame(self.master)
        mainFrame.pack()

        ### top frame ###
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        ### center frame ###
        centerFrame = Frame(mainFrame, width=1350, relief=RIDGE, bg='#f0f0f0', height=680)
        centerFrame.pack(side=TOP)

        ### center left frame ###
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)

        ### center right frames ###
        centerRightFrame = Frame(centerFrame, width=450, heigh=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack()

        ### searchBar ###
        searchBar = LabelFrame(centerRightFrame, width=440, height=75, text='SearchBar', bg="#9bc9ff")
        searchBar.pack(fill=BOTH)

        self.lblSearch = Label(searchBar, text="Search :", font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lblSearch.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search =Entry(searchBar, width=30, bd=3)
        self.ent_search.grid(row=0, column=1,columnspan=3, padx=10, pady=10)
        self.btnSearch = Button(searchBar, text="Search", font="arial 12 bold", bg="#fcc324", fg='white')
        self.btnSearch.grid(row=0, column=4, padx=20, pady=10)

        ### List Bar ###
        listBar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        listBar.pack(fill=BOTH)
        lbl_list = Label(listBar, text="Sort By", font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.listChoice=IntVar()
        rb1=Radiobutton(listBar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2=Radiobutton(listBar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3=Radiobutton(listBar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(listBar, text="List Books", bg='#2488ff', fg='white', font="arial 12 bold")
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        ### image info ###
        imageBar = Frame(centerRightFrame, width=440, height=350)
        imageBar.pack(fill=BOTH)
        self.title_right = Label(imageBar, text="Welcome to out library", font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = PhotoImage(file='icons/library.png')
        self.lblImage = Label(imageBar, image=self.img_library)
        self.lblImage.grid(row=1)

        ### Add Book ###
        self.iconbook = PhotoImage(file='icons/add_book.png')
        self.btnbook = Button(topFrame, text="Add Book", image=self.iconbook, compound=LEFT, font='arial 12 bold', command=self.addTheBook) 
        self.btnbook.pack(side=LEFT, padx=10)

        ### Add Member Button ###
        self.iconmember = PhotoImage(file='icons/users.png')
        self.btnmember=Button(topFrame, text="Add Member", font='arial 12 bold', padx=10)
        self.btnmember.configure(image=self.iconmember, compound=LEFT)
        self.btnmember.pack(side=LEFT)

        ### Give Book ###
        self.iconGive = PhotoImage(file='icons/givebook.png')
        self.btngive=Button(topFrame, text='Add Member', font='arial 12 bold', padx=10, image=self.iconGive, compound=LEFT)
        self.btngive.pack(side=LEFT)

        ### Tabs ###
        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon=PhotoImage(file='icons/books.png')
        self.tab2_icon=PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="Library Management", image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text="Statistic", image=self.tab2_icon, compound=LEFT)

        ### list books ###
        self.list_books= Listbox(self.tab1,width=40,height=30,bd=5,font='times 12 bold')
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)

        ### list Details ###
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)

        ### Statistic ###
        self.lbl_book_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

    def addTheBook(self):
        add = addBook.AddBook()



def main():
    root= Tk()
    app= Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.mainloop()

if __name__ == '__main__':
    main()