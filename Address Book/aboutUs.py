from tkinter import *

class About:
    def __init__(self, root):
        self.root = root

        frame=Frame(root, bg='#ffa500', width=550, height=550)
        frame.pack(fill=BOTH)
        text=Label(frame, text="Belajar menggunakan tkinter \ndalam membuat sebuah GUI pada python", bg="#ffa500", font='arial 15 bold')
        text.place(x=50, y=50)
    
def main():
    root = Tk()
    app = About(root)
    root.title("About Us")
    root.geometry("550x550+550+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()