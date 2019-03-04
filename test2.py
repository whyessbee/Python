from tkMessageBox import *
from Tkinter import *

import sqlite3
root=Tk()

con=sqlite3.Connection('logcount')
cur=con.cursor()
cur.execute('create table if not exists customer (custid number(11))')
    
Label(root,text='Select Your Breakfast',relief='ridge',font='Times 20 bold italic',bg='grey',).grid(row=0,column=3)
Label(root,text='Breakfast Calculator',font='Times 15 bold italic').grid(row=2,column=3)
Label(root,text='Name:').grid(row=3,column=0)
Label(root,text='Customer Code:').grid(row=3,column=5)
f=Entry(root)
f.grid(row=3,column=8)
e=Entry(root)
e.grid(row=3,column=3)
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()
v10=IntVar()
v11=IntVar()
v12=IntVar()
v13=IntVar()
v14=IntVar()
v15=IntVar()
v16=IntVar()
Checkbutton(root,text='Macroni($15)',variable=v1,onvalue=15,offvalue=0).grid(row=4,column=0)
Checkbutton(root,text='Pav Bhaji($11)',variable=v2,onvalue=11,offvalue=0).grid(row=4,column=3)
Checkbutton(root,text='Sandwich($8)',variable=v3,onvalue=8,offvalue=0).grid(row=5,column=0)
Checkbutton(root,text='Pasta($8)',variable=v4,onvalue=8,offvalue=0).grid(row=5,column=3)
Checkbutton(root,text='Aloo Paratha($20)',variable=v5,onvalue=20,offvalue=0).grid(row=6,column=0)
Checkbutton(root,text='Omlete($3)',variable=v6,onvalue=3,offvalue=0).grid(row=6,column=3)
Checkbutton(root,text='Poha($5)',variable=v7,onvalue=5,offvalue=0).grid(row=7,column=0)
Checkbutton(root,text='Fruits($4)',variable=v8,onvalue=4,offvalue=0).grid(row=7,column=3)
Checkbutton(root,text='Noodles($12)',variable=v9,onvalue=12,offvalue=0).grid(row=8,column=0)
Checkbutton(root,text='Bread Butter($2)',variable=v10,onvalue=2,offvalue=0).grid(row=8,column=3)
Checkbutton(root,text='Egg($2)',variable=v11,onvalue=2,offvalue=0).grid(row=9,column=0)
Checkbutton(root,text='Sprouts($6)',variable=v12,onvalue=6,offvalue=0).grid(row=9,column=3)
Checkbutton(root,text='Idli($6)',variable=v13,onvalue=6,offvalue=0).grid(row=10,column=0)
Checkbutton(root,text='Porage($6)',variable=v14,onvalue=6,offvalue=0).grid(row=10,column=3)
Checkbutton(root,text='Upama($7)',variable=v15,onvalue=7,offvalue=0).grid(row=11,column=0)
Checkbutton(root,text='Macroni($2)',variable=v16,onvalue=2,offvalue=0).grid(row=11,column=3)
def check():
    cur.execute('insert into customer values (?)',(f.get()))
    a=cur.execute('select count(custid) from customer where custid=?',(f.get()))
    x=a.fetchone()[0]
    
    a=v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get()+v11.get()+v12.get()+v13.get()+v14.get()+v15.get()+v16.get()
    if x>10:
        
        b=a*0.9
        Label(root,text='Hellow Mr/Ms.'+' '+e.get()+' '+',Your Total Amount After 10% Discount:'+' '+ str(int(b))+'$',font='Times 15 bold italic').grid(row=15,column=0)
        Label(root,text='Please visit us again!!!!!').grid(row=16,column=0)
    elif x<=10:
            
        
        Label(root,text='Hellow Mr/Ms.'+' '+e.get()+' '+',Your Total Amount:'+' '+ str(int(a))+'$',font='Times 15 bold italic').grid(row=15,column=0)
        Label(root,text='Please visit us again!!!!!').grid(row=16,column=0)
def exit():
    root.destroy()
def showcount():
    
    a=cur.execute('select count(custid) from customer where custid=?',(f.get()))
    x=a.fetchone()
    
    showinfo('info',x)
    
Button(root,text='Exit',command=exit).grid(row=12,column=3)
Button(root,text='Check',command=check).grid(row=12,column=0)        
Button(root,text='count check',command=showcount).grid(row=12,column=5)
root.mainloop()
