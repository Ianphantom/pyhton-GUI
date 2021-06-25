from tkinter import *

root=Tk()
root.title("Calculator App") 
root.geometry("380x550+850+200")

### Function ###
def enterNumber(x):
    if(entry_box.get()== "O"):
        entry_box.delete(0, "end")
        entry_box.insert(0, str(x))
    else:
        lenght=len(entry_box.get())
        entry_box.insert(lenght, str(x))


def enterOperator(x):
    if entry_box.get() != "O":
        lenght = len(entry_box.get())
        entry_box.insert(lenght, btn_operator[x]['text'])

def funcClear():
    entry_box.delete(0, END)
    entry_box.insert(0, "O")

def funcOperator():
    pass

def funcDelete():
    length = len(entry_box.get())
    entry_box.delete(length-1,'end')
    if length == 1:
        entry_box.insert(0, "O")


### EntryBox ###
entry_box = Entry(font='verdana 14 bold', width=22, bd=10, justify=RIGHT, bg='#e6e6fa')
entry_box.insert(0, "O")
entry_box.place(x=20, y=10)

### Buttons ###
btn_numbers=[]
for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), font='times 15 bold', bd=5, command= lambda x=i:enterNumber(x)))

btn_text=1

for i in range(0,3):
    for j in range (0,3):
        btn_numbers[btn_text].place(x=25+j*90, y=70+i*70)
        btn_text += 1
 
### Operator Button ###
btn_operator=[]
for i in range(4):
    btn_operator.append(Button(width=4, font='times 15 bold', bd=5, command = lambda x=i:enterOperator(x))) 

btn_operator[0]['text'] = "+"
btn_operator[1]['text'] = "-"
btn_operator[2]['text'] = "*"
btn_operator[3]['text'] = "/"

for i in range(4):
    btn_operator[i].place(x=290, y= 70+ i*70)

### Others Button ###

btn_zero = Button(width=19, font="times 15 bold", text="0", bd=5, command= lambda x = 0: enterNumber(x))
btn_zero.place(x=25, y=280)
btn_clear = Button(width=4, font="times 15 bold", text="C", bd=5, command=funcClear)
btn_clear.place(x=25, y=340)
btn_dot = Button(width=4, text=".", font='times 15 bold', bd=5, command=lambda x=".":enterNumber(x))
btn_dot.place(x=115, y=340)
btn_equal = Button(width=4, text="=", font='times 15 bold', bd=5, command=funcOperator)
btn_equal.place(x=205, y=340)
btn_delete = Button(width=4, text="DEL", font='times 15 bold', bd=5, command=funcDelete)
btn_delete.place(x=290, y=340)
root.mainloop()