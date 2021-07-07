from tkinter import *
from tkinter import ttk
import sqlite3
import addBook
import addMember

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
        self.btnSearch = Button(searchBar, text="Search", font="arial 12 bold", bg="#fcc324", fg='white', command=self.searchBooks)
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
        btn_list = Button(listBar, text="List Books", bg='#2488ff', fg='white', font="arial 12 bold", command=self.listBooks)
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
        self.btnmember=Button(topFrame, text="Add Member", font='arial 12 bold', padx=10, command=self.addTheMember)
        self.btnmember.configure(image=self.iconmember, compound=LEFT)
        self.btnmember.pack(side=LEFT)

        ### Give Book ###
        self.iconGive = PhotoImage(file='icons/givebook.png')
        self.btngive=Button(topFrame, text='Give Book', font='arial 12 bold', padx=10, image=self.iconGive, compound=LEFT)
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
        
        def displayBook(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count=0
            for book in books:
                self.list_books.insert(count, str(book[0])+ "-" +str(book[1]))
                count += 1
            
            def bookInfo(evt):
                self.list_details.delete(0, END)
                value = str(self.list_books.get(self.list_books.curselection()))
                # print(value)
                id=value.split('-')[0]
                # print(id)
                book =cur.execute('SELECT * FROM books WHERE book_id=?', (id,))
                book_info= book.fetchall()
                # print(book_info)
                self.list_details.insert(0,"Book Name : "+ str(book_info[0][1]))
                self.list_details.insert(1,"Author : "+ str(book_info[0][2]))
                self.list_details.insert(2,"Page : "+ str(book_info[0][3]))
                self.list_details.insert(3,"Language : "+ str(book_info[0][4]))
                if book_info[0][5] != 0 :
                    self.list_details.insert(4, "Status : Already Borrowed")
                else:
                    self.list_details.insert(4, "Status : Available")

            self.list_books.bind('<<ListboxSelect>>', bookInfo)

        displayBook(self)

    def addTheBook(self):
        add = addBook.AddBook()

    def addTheMember(self):
        member = addMember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0, END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0])+ "-" + str(book[1]))
            count += 1

    def listBooks(self):
        value = self.listChoice.get()
        self.list_books.delete(0, END)
        if value == 1:
            allbooks = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in allbooks:
                self.list_books.insert(count, str(book[0]) +"-"+ str(book[1]))
                count+=1
        elif value ==2 :
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status=?", (0,)).fetchall()
            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0]) +"-"+ str(book[1]))
                count+=1
        else :
            books_borrowed = cur.execute("SELECT * FROM books WHERE book_status=?", (1,)).fetchall()
            count = 0
            for book in books_borrowed:
                self.list_books.insert(count, str(book[0]) +"-"+ str(book[1]))
                count+=1


def main():
    root= Tk()
    app= Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.mainloop()

if __name__ == '__main__':
    main()