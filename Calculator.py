
from tkinter import *
from tkinter import ttk
import os


root = Tk()
root.title('Calculator')
root.geometry('312x319')
root.resizable(0, 0)

global a, opr, b, historyWindow, entire_eq, canvas

a, opr, b, entire_eq = '', '', '', ''

def change(exp):
    history = open('history.txt', 'a')
    history.write('\n'+exp)
    history.close()

def cll():
    try:
        os.remove("history.txt")
    except:
        pass
    historyWindow.destroy()

def btn_histy(text):
    global a, opr, b, entire_eq, historyWindow
    
    x = text.split('=')[1]
    b, opr = '', ''
    
    a = eval(x)
    input_text.set(x)
    historyWindow.destroy()
    

def mouse(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def click_btt(item):
    global a, opr, b, entire_eq, historyWindow
    
    if item in [0,1,2,3,4,5,6,7,8,9, '.']:

        if opr == '':

            if item == '.':
                if a == '' or a == '0.':
                    a = ('0.')
                    input_text.set(a)

                else:
                    a = (str(a)+str(item))
                    input_text.set(a)
            else:
                a = eval(str(a)+str(item))
                input_text.set(a)


        else:
            if item == '.':
                if b == '' or b == '0.':
                    b = ('0.')
                    input_text.set(b)

                else:
                    b = (str(b)+str(item))
                    input_text.set(b)
            else:
                b = eval(str(b)+str(item))
                input_text.set(b)

                            
    elif item == 'ac':
        input_text.set('')
        a = ''
        b = ''
        opr = ''



    elif item == 'history':
        global canvas
        historyWindow = Toplevel(root)

        historyWindow.title('History')
        historyWindow.geometry('332x319')
        historyWindow.resizable(0, 0)

        topFrm = Frame(historyWindow,relief=GROOVE,bd=1)
        topFrm.pack()
        canvas = Canvas(topFrm, width=310)
        canvas.pack(side = 'left', fill='both', expand='1')     
        myscrollbar=Scrollbar(topFrm,orient="vertical",command=canvas.yview)
        myscrollbar.pack(side="right",fill="y")
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox('all')))
        canvas.bind_all("<MouseWheel>", mouse)
        frame2 = Frame(canvas)
        canvas.create_window((0,0),window=frame2,anchor='nw')
        
        try:
            file = open('history.txt', 'r')
            lines = file.readlines()
            file.close()
            eqs = []
            for i in lines:
                if i != '\n':
                    eqs.append(i)
            btns = [] 
            for eq in eqs:
                idx = eqs.index(eq)
                btns.append(Button(frame2, text=eq.strip(), width=38, font=('Calibri', 12), command=lambda c=idx: btn_histy(btns[c].cget('text'))))
                btns[idx].pack()
            cll_btn = Button(historyWindow, bg='grey', fg='white',text = 'Clear History', font=('Times New Roman', 14), command=cll)
            cll_btn.place(x=100, y=275)   
        except:
            no_lbl = Label(historyWindow, text='No History Found.', font=('Times New Roman', 14))
            no_lbl.place(x=90 ,y=125)
            
        historyWindow.grab_set()

    elif item == '=':      
        if a != '' and opr != '' and b != '':
            
            if opr == '+':
                exp = (a)+(b)
                input_text.set(exp)
                
            elif opr == '-':
                exp = (a)-(b)
                input_text.set(exp)
                
            elif opr == 'x':
                exp = (a)*(b)
                input_text.set(exp)
                
            elif opr == '÷':
                exp = (a)/(b)
                input_text.set(exp)

            if entire_eq == '':
                x = '('+str(a)+str(opr)+str(b)+')'+'='+str(exp)
                change(x)

            else:
                x = '('+str(entire_eq)+str(opr)+str(b)+')'+'='+str(exp)
                change(x)

            a, opr, b, entire_eq = exp, '', '', ''

    else:

        if b == '':
           opr = item

        elif a != '' and opr != '' and b != '':
            if opr == '+':
                exp = (a)+(b)
                eq = str(a)+str(opr)+str(b)
                
                if entire_eq == '':
                    entire_eq = '('+str(eq)+')'
                    
                else:
                    entire_eq = '('+str(entire_eq)+str(opr)+str(b)+')'

                input_text.set(exp)                
                a = exp
                opr = item
                b = ''
                
            elif opr == '-':
                exp = (a)-(b)
                eq = str(a)+str(opr)+str(b)

                if entire_eq == '':
                    entire_eq = '('+str(eq)+')'
                    
                else:
                    entire_eq = '('+str(entire_eq)+str(opr)+str(b)+')'
                
                input_text.set(exp)
                a = (exp)
                opr = item
                b = ''
                
            elif opr == 'x':
                exp = (a)*(b)

                eq = str(a)+str(opr)+str(b)

                if entire_eq == '':
                    entire_eq = '('+str(eq)+')'
                    
                else:
                    entire_eq = '('+str(entire_eq)+str(opr)+str(b)+')'
                
                input_text.set(exp)
                a = exp
                opr = item
                b = ''
                
            elif opr == '÷':
                exp = (a)/(b)

                eq = str(a)+str(opr)+str(b)

                if entire_eq == '':
                    entire_eq = '('+str(eq)+')'
                    
                else:
                    entire_eq = '('+str(entire_eq)+str(opr)+str(b)+')'
                    
                input_text.set(exp)
                a = exp
                opr = item
                b = ''
            
            
digcolor = '#fff'
optcolor = '#eee'

input_text = StringVar()
input_frame = Frame(root, width=312,height=50, bd=0)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50, bg=optcolor, bd=0, justify=RIGHT, state='readonly')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg='grey')
btns_frame.pack()


#First Row----------------------------------------------------------------------------------------------
seven = Button(btns_frame, text ='7', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(7)).grid(row=0, column=0,padx=1,pady=1)
eight = Button(btns_frame, text ='8', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(8)).grid(row=0, column=1,padx=1,pady=1)
nine = Button(btns_frame, text ='9', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(9)).grid(row=0, column=2,padx=1,pady=1)
add = Button(btns_frame, text ='+', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt('+')).grid(row=0, column=3,padx=1,pady=1)


#Second Row----------------------------------------------------------------------------------------------
four = Button(btns_frame, text ='4', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(4)).grid(row=1, column=0,padx=1,pady=1)
five = Button(btns_frame, text ='5', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(5)).grid(row=1, column=1,padx=1,pady=1)
six = Button(btns_frame, text ='6', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(6)).grid(row=1, column=2,padx=1,pady=1)
minus = Button(btns_frame, text ='-', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt('-')).grid(row=1, column=3,padx=1,pady=1)


#third Row----------------------------------------------------------------------------------------------
one = Button(btns_frame, text ='1', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(1)).grid(row=2, column=0,padx=1,pady=1)
two = Button(btns_frame, text ='2', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(2)).grid(row=2, column=1,padx=1,pady=1)
three = Button(btns_frame, text ='3', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(3)).grid(row=2, column=2,padx=1,pady=1)
multiply = Button(btns_frame, text ='x', fg='black', width=10, height=3, bd=0, bg=optcolor, cursor='hand2',
                command=lambda: click_btt('x')).grid(row=2, column=3,padx=1,pady=1)


#Fourth Row----------------------------------------------------------------------------------------------
zero = Button(btns_frame, text ='0', fg='black', width=10, height=3, bd=0, cursor='hand2',
                command=lambda: click_btt(0)).grid(row=3, column=0, padx=1,pady=1)

point = Button(btns_frame, text ='.', fg='black', width=10, height=3, bd=0, bg=optcolor, cursor='hand2',
                command=lambda: click_btt('.')).grid(row=3, column=1,padx=1,pady=1)
ac = Button(btns_frame, text ='AC', fg='black', width=10, height=3, bd=0, bg=optcolor, cursor='hand2',
                command=lambda: click_btt('ac')).grid(row=3, column=2,padx=1,pady=1)
divide = Button(btns_frame, text ='÷', fg='black', width=10, height=3, bd=0, bg=optcolor, cursor='hand2',
                command=lambda: click_btt('÷')).grid(row=3, column=3,padx=1,pady=1)


#Fifth Row----------------------------------------------------------------------------------------------
history = Button(btns_frame, text="History", fg="black", width=32, height=3, bd=0, bg=optcolor, cursor='hand2',
               command=lambda: click_btt('history')).grid(row=4, column=0, columnspan=3, padx=1, pady=1)
equals = Button(btns_frame, text ='=', fg='black', width=10, height=3, bd=0, bg=optcolor, cursor='hand2',
                command=lambda: click_btt('=')).grid(row=4, column=3,padx=1,pady=1)

root.mainloop()
