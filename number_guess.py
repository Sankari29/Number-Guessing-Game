from tkinter import *
import random

rand=Tk()
rand.title('NUMBER GUESSING GAME')
rand.geometry('700x500')
rand.config(bg='orange')

randNum=random.randint(0,20)
chance=3
var=IntVar()
disp=StringVar()


def check_guess():
    global randNum
    global chance
    usr_ip=var.get()
    if chance>0:
        if usr_ip==randNum:
            msg=f'YOU WON!! {randNum} is the right answer.'
        elif usr_ip>randNum:
            chance=chance-1
            msg=f'{usr_ip} is greater.You have {chance} attempt only left. '
        elif usr_ip<randNum:
            chance=chance-1
            msg=f'{usr_ip} is smaller.You have {chance} attempt only left'
        else:
            msg='Oops...Something went wrong!!'
    else:
        msg=f'You lost! keep try man'
    disp.set(msg)


Label(rand,text='Number Guessing Game from 0 to 20',font=('Arial', 28 , 'bold'),padx=10,pady=10,bg='blue').pack(pady=(10,0))
Entry(rand,textvariable=var,font=('Arial', 20)).pack(pady=(50,10))
Button(rand,text='submit',font=('Arial' ,24),command=check_guess).pack()
Label(rand,textvariable=disp,bg='white',font=('Arial',20)).pack(pady=(20,0))

rand.mainloop()
