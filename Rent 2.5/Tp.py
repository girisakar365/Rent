from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter.tix import *

#RNTMDL
from Bridge import *
from db import db
#RNTMDL


class Display:

    def display_result(win,table,data=[0,0,0,0,0,0]):
        #ButtonImage
        delete_record = ImageTk.PhotoImage(file='__img__\\delete_record.ico')
        edit_record = ImageTk.PhotoImage(file='__img__\\edit_record.ico')
        
        #TextLabel
        Include.txt(win,text='Status:   Active',fontSize=12,x=690,y=315)

        #Buttons
            #deletebutton
        def delete():
            db.delete_table(table)
            Include.txt(win,text='Status: Deleted',fontSize=12,x=690,y=315)
        delete_button = Button(win,image=delete_record,borderwidth=0,bg='#ffffff',activebackground='#ed1c23',
        command=lambda:[Include.conform(win,delete,'RENT','Are you sure you want to delete this record?')])
        delete_button.image = delete_record
        delete_button.place(x=690,y=535)
        
            #editbutton
        edit_button = Button(win,image=edit_record,borderwidth=0,bg='#ffffff',activebackground='#cecece',command=lambda:[Subwin.editdata()])
        edit_button.image = edit_record
        edit_button.place(x=750,y=535)

        #TreeView
        tv = ttk.Treeview(win)

        tv['columns'] = ('Catagory','Amount')

        tv.column('#0',width=50,minwidth=25)
        tv.column('Catagory',anchor=CENTER,width=380)
        tv.column('Amount',anchor=W,width=120)
        tv.heading('#0',text='S.N',anchor=W)
        tv.heading('Catagory',text='Catagory',anchor=CENTER)
        tv.heading('Amount',text='Amount',anchor=W)

        results = list(data)
        tv.insert(parent='',index='end',iid=0,text='1)',value=('Electricity',results[1]))
        tv.insert(parent='',index='end',iid=1,text='2)',value=('Water',results[2]))
        tv.insert(parent='',index='end',iid=2,text='3)',value=('Waste',results[3]))
        tv.insert(parent='',index='end',iid=3,text='4)',value=('Rent',results[4]))
        tv.insert(parent='',index='end',iid=4,text='5)',value=('Total Amount',results[5]))
        tv.place(x=690,y=365,height=160,width=500)

class Subwin:


    def password():

        #MiniWinSetup
        miniwin00 = Toplevel()
        miniwin00.grab_set()
        miniwin00.attributes('-alpha',0.86)
        miniwin00.title('Security')
        miniwin00.geometry('400x300+500+230')
        miniwin00.resizable(0,0)
        miniwin00.config(bg='#fdfddb')
        miniwin00.iconbitmap('__img__\\change_password.ico')

        #imagesetup
        conform = ImageTk.PhotoImage(file="__img__\\next.png")
        global show
        nshow =ImageTk.PhotoImage(file="__img__\\nshow.png")

        #Lables
        Include.txt(miniwin00,text='  Security',fontSize=40,bg='#fdfddb',x=50,y=5)

        Include.txt(miniwin00,text='Current Password',bg='#fdfddb',fontStyle='Times New Roman',x=5,y=95)
        
        Include.txt(miniwin00,text='New Password',bg='#fdfddb',fontStyle='Times New Roman',x=5,y=145)

        Include.txt(miniwin00,text='Re-Enter Password',bg='#fdfddb',fontStyle='Times New Roman',x=5,y=200)

        #Entries
        recent_password = Entry(miniwin00,width=30,borderwidth=2,show='*')
        recent_password.place(x=170,y=100)
        #Include.tip(miniwin00,recent_password,'Type current password')
        Include.eye(miniwin00,recent_password,x=360,y=100)

        new_password = Entry(miniwin00,width=30,borderwidth=2,show='*')
        new_password.place(x=170,y=150)
        #Include.tip(miniwin00,new_password,'Type new password')
        Include.eye(miniwin00,new_password,x=360,y=150)

        re_password = Entry(miniwin00,width=30,borderwidth=2,show='*')
        re_password.place(x=170,y=205)
        #Include.tip(miniwin00,re_password,'Re-type new password')
        Include.eye(miniwin00,re_password,x=360,y=205)

        #Buttons
        def renew_pascode():
            OAJ.renew(miniwin00,recent_password.get(),new_password.get(),re_password.get())
        conf00 = Button(miniwin00,image=conform,bg='#fdfddb',borderwidth=0,
        command=lambda:[Include.conform(miniwin00,renew_pascode,'Security','Change Password?')])
        conf00.image=conform
        #Include.tip(miniwin00,conf00,'Conform')
        conf00.place(x=360,y=260)

        # root.mainloop

    def editdata():
        #winsetup
        miniwin01 = Toplevel()
        miniwin01.grab_set()
        miniwin01.attributes('-alpha',0.86)
        miniwin01.title('Edit Record')
        miniwin01.iconbitmap('__img__\\logo.ico')
        miniwin01.geometry('400x500+500+100')
        miniwin01.resizable(0,0)
        miniwin01.config(bg='#fdfddb')

    
        #image
        electricity_logo = ImageTk.PhotoImage(file='__img__\\electric-meter.png')
        water_logo = ImageTk.PhotoImage(file='__img__\\water_meter.png')
        waste_logo =ImageTk.PhotoImage(file='__img__\\garbage.png')
        rent_mini_logo = ImageTk.PhotoImage(file='__img__\\real-estate.png')
        conform = ImageTk.PhotoImage(file="__img__\\next.png")
        
        #Label 
        Include.txt(miniwin01,text='Edit Section',bg='#fdfddb',fontSize=30,x=30,y=30)

        #Entries
        bg = Label(miniwin01,image=electricity_logo,bg='#fdfddb')
        bg.image=electricity_logo
        bg.place(x=60,y=90)
        e_m00 = Entry(miniwin01,width=20,borderwidth=2)
        e_m00.place(x=20,y=130)
        e_m01 = Entry(miniwin01,width=20,borderwidth=2)
        e_m01.place(x=20,y=170)

        bg = Label(miniwin01,image=water_logo,bg='#fdfddb')
        bg.image=water_logo
        bg.place(x=260,y=90)
        w_m00 = Entry(miniwin01,width=20,borderwidth=2)
        w_m00.place(x=220,y=130)
        w_m01 = Entry(miniwin01,width=20,borderwidth=2)
        w_m01.place(x=220,y=170)

        Include.txt(miniwin01,' Default Entries',bg='#fdfddb',fontSize=25,x=10,y=230)
        bg = Label(miniwin01,image=waste_logo,width=20,bg='#fdfddb')
        bg.image = waste_logo
        bg.place(x=60,y=290)
        waste = Entry(miniwin01,width=20,borderwidth=2)
        waste.place(x=20,y=330)
        waste.insert(0,175)
        
        bg = Label(miniwin01,image=rent_mini_logo,bg='#fdfddb')
        bg.image = rent_mini_logo
        bg.place(x=260,y=290)
        rent = Entry(miniwin01,width=20,borderwidth=2)
        rent.place(x=220,y=330)
        rent.insert(0,14000)

        w_constant = Entry(miniwin01,width=10,borderwidth=2)
        w_constant.place(x=140,y=380)
        w_constant.insert(0,200)

        global hold
        hold = IntVar()
        u00 = Checkbutton(miniwin01, text='11',variable=hold,onvalue=11,offvalue=0)
        u01 = Checkbutton(miniwin01,text='12',variable=hold,onvalue=12,offvalue=0)
        u00.config(borderwidth=0,bg='#fdfddb',activebackground='#cecece')
        u01.config(borderwidth=0,bg='#fdfddb',activebackground='#cecece')
        u00.place(x=140,y=420)
        u01.place(x=180,y=420)

        def somthing():
            messagebox.showinfo('RENT','Construction going on.',parent=miniwin01)
        conf00 = Button(miniwin01,image=conform,bg='#fdfddb',borderwidth=0,
        command=lambda:[Include.conform(miniwin01,somthing,'Edit Record','Conform Edit Record ?')])
        conf00.image=conform
        conf00.place(x=360,y=460)