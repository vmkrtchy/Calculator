import tkinter as tk

def add_d(digit):
    value = calc.get()
    if len(value) == 1 and value == '0':
        value = value[1:]
    elif len(value) > 1 and value[0] == '0' and value[1] != '.':
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value + digit)

def add_operation(operator):

    value = calc.get()
    
    if value[-1] in '-+/*': 
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
        
    calc.delete(0,tk.END)
    calc.insert(0,value+operator)

def make_vid(tver):
    return tk.Button(text=tver,command=lambda : add_d(tver))

def make_operator(operator):
    return tk.Button(text=operator,
                     fg='red',
                     command=lambda : add_operation(operator))

def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value+value[:-1]
        
        
    calc.delete(0,tk.END)
    calc.insert(0, eval(value))

def make_calc_button(operation):
    return tk.Button(  
                        text=operation,
                        fg='red',
                        command=calculate
                    )
def rm():
    calc.delete(0,tk.END)
    calc.insert(0, 0)
def make_rm_button(operation):
    return tk.Button(  
                        text=operation,
                        fg='red',command=rm
                    )    
    
win = tk.Tk()
win.geometry(f'240x315+100+200')
win['bg'] = '#45f0e9'
win.title('Calculator')

calc = tk.Entry(win,justify=tk.RIGHT)
calc.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky='we',
            padx=5,
            pady=5
        )
calc.insert(0, '0')


make_vid('1').grid(row=1,column=0,stick='wens',padx=2,pady=2)
make_vid('2').grid(row=1,column=1,stick='wens',padx=2,pady=2)
make_vid('3').grid(row=1,column=2,stick='wens',padx=2,pady=2)
make_vid('4').grid(row=2,column=0,stick='wens',padx=2,pady=2)
make_vid('5').grid(row=2,column=1,stick='wens',padx=2,pady=2)
make_vid('6').grid(row=2,column=2,stick='wens',padx=2,pady=2)
make_vid('7').grid(row=3,column=0,stick='wens',padx=2,pady=2)
make_vid('8').grid(row=3,column=1,stick='wens',padx=2,pady=2)
make_vid('9').grid(row=3,column=2,stick='wens',padx=2,pady=2)
make_operator('0').grid(row=4,column=0,stick='wens',padx=2,pady=2)

make_operator('+').grid(row=1,column=3,stick='wens',padx=5,pady=5)
make_operator('-').grid(row=2,column=3,stick='wens',padx=5,pady=5)
make_operator('*').grid(row=3,column=3,stick='wens',padx=5,pady=5)
make_operator('/').grid(row=4,column=3,stick='wens',padx=5,pady=5)
make_vid('.').grid(row=4,column=1,stick='wens',padx=5,pady=5)


make_calc_button('=').grid(row=4,column=2,sticky='wens',padx=5,pady=5)
make_rm_button('C').grid(row=5,column=0,sticky='wens',padx=5,pady=5,columnspan=4)


win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)
win.grid_columnconfigure(4,minsize=60)



win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
# win.grid_rowconfigure(3,minsize=60)
# win.grid_rowconfigure(3,minsize=60)


win.mainloop()