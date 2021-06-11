from tkinter import *

win = Tk()
win.geometry('400x450')

global result
result = ""

ec = StringVar()

def clear():
    global ec,result
    txt1.delete(0, "end")
    result = ""
    ec.set("")


def press(z):
    global result,resultT
    resultT = result
    result = result + str(z)
    ec.set(result)

def equal():
    try:
        global result, x
        x = str(eval(result))
        result = x
        ec.set(x)
    except:
        ec.set("Error..")

def p():
    global p
    p= 3.14


txt1= Entry(win, width= 50, text= ec)
txt1.grid(pady= 15, padx= 10, columnspan= 3)
btn1= Button(win, text= "1", width= 10, height=5, command= lambda:press(1))
btn1.grid(column= 0, row= 1)
btn2= Button(win, text= "2", width= 10, height=5, command= lambda:press(2))
btn2.grid(column= 1, row= 1)
btn3= Button(win, text= "3", width= 10, height=5, command= lambda:press(3))
btn3.grid(column= 2, row= 1)
btn4= Button(win, text= "4", width= 10, height=5, command= lambda:press(4))
btn4.grid(column= 0, row= 2)
btn5= Button(win, text= "5", width= 10, height=5, command= lambda:press(5))
btn5.grid(column= 1, row= 2)
btn6= Button(win, text= "6", width= 10, height=5, command= lambda:press(6))
btn6.grid(column= 2, row= 2)
btn7= Button(win, text= "7", width= 10, height=5, command= lambda:press(7))
btn7.grid(column= 0, row= 3)
btn8= Button(win, text= "8", width= 10, height=5, command= lambda:press(8))
btn8.grid(column= 1, row= 3)
btn9= Button(win, text= "9", width= 10, height=5, command= lambda:press(9))
btn9.grid(column= 2, row= 3)
btnC= Button(win, text= "C", width= 10, height=5, command= clear)
btnC.grid(column= 0, row= 4)
btnD= Button(win, text= "/", width= 10, height=5, command=lambda:press("/") )
btnD.grid(column= 3, row= 1)
btnM= Button(win, text= "*", width= 10, height=5, command=lambda:press("*"))
btnM.grid(column= 3, row= 2)
btnS= Button(win, text= "-", width= 10, height=5, command=lambda:press("-"))
btnS.grid(column= 3, row= 3)
btnA= Button(win, text= "+", width= 10, height=5, command=lambda:press("+"))
btnA.grid(column= 3, row= 4)
btnE= Button(win, text= "=", width= 10, height=5, command= equal)
btnE.grid(column= 2, row= 4)
btnP= Button(win, text= "π", width= 10, height=5, command= lambda:press(3.14))
btnP.grid(column= 1, row= 4)

win.mainloop()