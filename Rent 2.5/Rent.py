#__BUILD-IN's__#
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import date

#__R-MODULE's__#
from Bridge import *
from Tp import *
from db import *


dd = date.today()
Month = dd.strftime('%B')
Year = dd.strftime('%Y')
Date = dd.strftime('%B-%Y')
Meter = [0]


def Rent():
    #windows_type
    root.attributes('-alpha',0.9)
    root.title(' RENT')
    root.iconbitmap('__img__\\logo.ico')
    root.attributes('-topmost',0)
    root.geometry('1230x700+100+10')
    root.resizable(0,0)

    #image_imports
        #background_images
    background = ImageTk.PhotoImage(file='__img__\\background.jpg')
    record = ImageTk.PhotoImage(file='__img__\\record.ico')
        #icon_images
    password_change = ImageTk.PhotoImage(file='__img__\\change_password.ico') 
    search = ImageTk.PhotoImage(file='__img__\\search.png')
    electricity_logo = ImageTk.PhotoImage(file='__img__\\electric-meter.png')
    water_logo = ImageTk.PhotoImage(file='__img__\\water_meter.png')
    waste_logo =ImageTk.PhotoImage(file='__img__\\garbage.png')
    rent_mini_logo = ImageTk.PhotoImage(file='__img__\\real-estate.png')

    #Labels
        #image_label
    bg = Label(root,image=background)
    bg.image = background
    bg.pack()

    bg = Label(root,image=electricity_logo,width=25,bg='#bbbbbb')
    bg.image = electricity_logo
    bg.place(x=85,y=270)
    #Include.tip(root,bg,'Flat Electricity Meter')

    bg = Label(root,image=water_logo,width=30,bg='#b3d4e8')
    bg.image = water_logo
    bg.place(x=325,y=270)
    #Include.tip(root,bg,'Water Electricity Meter')

    bg = Label(root,image=waste_logo,width=20,bg='#d7d7d7')
    bg.image = waste_logo
    bg.place(x=80,y=470)
    #Include.tip(root,bg,'Waste')

    bg = Label(root,image=rent_mini_logo,bg='#ffffff3b93e7')
    bg.image = rent_mini_logo
    bg.place(x=340,y=470)
    #Include.tip(root,bg,'Rent')

        #digital clock
    Include.digital_clock(root,x=470,y=60)
        #text_label
    Include.txt(win=root,text='Search Section',fontSize=20,x=850,y=165)    
    Include.txt(win=root,text='Record Section',fontSize=18,x=50,y=165)

    #Entries

    e_m00 = Entry(root,width=20,borderwidth=2)
    e_m00.place(x=50,y=330)
    #Include.tip(root,e_m00,'Previous Meter')
    e_m01 = Entry(root,width=20,borderwidth=2)
    e_m01.place(x=50,y=400)
    #Include.tip(root,e_m01,'Present Meter')
    e_m01.focus()

    w_m00 = Entry(root,width=20,borderwidth=2)
    w_m00.place(x=300,y=330)
    #Include.tip(root,w_m00,'Previous Meter')
    w_m01 = Entry(root,width=20,borderwidth=2)
    w_m01.place(x=300,y=400)
    #Include.tip(root,w_m01,'Present Meter')

    w_constant = Entry(root,width=10,borderwidth=2)
    w_constant.place(x=390,y=280)
    #Include.tip(root,w_constant,'Water Cost')
    # w_constant.insert(0,200)

    waste = Entry(root,width=20,borderwidth=2)
    waste.place(x=50,y=530)
    #Include.tip(root,waste,'Waste Cost')
    # waste.insert(0,175)

    rent = Entry(root,width=20,borderwidth=2)
    rent.place(x=300,y=530)
    #Include.tip(root,rent,'Rent Cost')
    # rent.insert(0,14000)

    #CheckBox
    hold = IntVar()
    def g():
        del Meter[0]
        Meter.append(hold.get()) 

    u00 = Checkbutton(root, text='11',variable=hold,onvalue=11,offvalue=0,command=g)
    u01 = Checkbutton(root,text='12',variable=hold,onvalue=12,offvalue=0,command=g)
    u00.config(borderwidth=0,bg='#ffffff',activebackground='#cecece')
    u01.config(borderwidth=0,bg='#ffffff',activebackground='#cecece')
    #Include.tip(root,u00,'Unit')
    #Include.tip(root,u01,'Unit')
    u00.place(x=300,y=362)
    u01.place(x=360,y=362)

    #ComboBox
    global month 
    global year
        #selectmonth
    s_00 = ['All',
    'January','February','March','April','May','June',
    'July','August','September','October','November','December']
    month = ttk.Combobox(root,value=s_00,width=10)
    month.current(0)
    month.bind('<<ComboboxSelected>>')
    month.config(state='readonly')
    #Include.tip(root,month,'Select Month')
    month.place(x=850,y=265)
        #selectyear
    s_01 = ['Year']
    start = 0
    for i in range(70):
        i = i+1
        start = 2017 + i
        s_01.append(start)
    year = ttk.Combobox(root,value=s_01,width=10)
    year.current(0)
    year.config(state='readonly')
    year.bind('<<ComboboxSelected>>')
    #Include.tip(root,year,'Select Year')
    year.place(x=960,y=265)
        

    #Buttons
    change_password = Button(root,image=password_change,bg='#ffffff',command=lambda:[Subwin.password()])
    change_password.config(activebackground='#cecece')
    #Include.tip(root,change_password,'Security')
    change_password.image = password_change
    change_password.place(x=10,y=10)

    def send():
        en = e_m01.get()
        ep = e_m00.get()
        wn = w_m01.get()
        wp = w_m00.get()
        wc = w_constant.get()
        wa = waste.get()
        re = rent.get()
        condition = OAJ.create_record(Date,en,ep,wn,wp,Meter[0],wc,wa,re)
        if condition == True:
            raw = db.dispaly_table(Date)
            if raw == False:
                pass 
            else:
                Display.display_result(root,Date,raw)
        else:
            pass
    creat_data = Button(root,image=record,borderwidth=0,bg='#ffffff',activebackground='#cecece',
    command=lambda:[Include.conform(root,send,'RENT','Are you sure you want to create this record?')])
    #Include.tip(root,creat_data,'Creat Record')
    creat_data.image = record
    creat_data.place(x=200,y=610)

    def searchQ():
        table = month.get()+'-'+year.get()
        data = db.dispaly_table(table)
        if data == False:
            pass
        else:
            Display.display_result(root,table=table,data=data)
    search_data = Button(root,image=search,bg='#ffffff',activebackground='#cecece',command=lambda:[searchQ()])
    #Include.tip(root,search_data,'Search Record')
    search_data.image = search
    search_data.place(x=1060,y=265)


root = Tk()
root.geometry('500x430+450+130')
root.title('LOG-IN')
root.iconbitmap('__img__\\Logo.ico')
root.grab_set()
root.attributes('-alpha',0.9)
root.resizable(0,0)
root.attributes('-topmost',1)#sets the window to front
root.config(bg='#fdfddb')

#fakewin 
fake = Toplevel()
fake.attributes('-alpha',0.9)
fake.title(' RENT')
fake.iconbitmap('__img__\\logo.ico')
fake.geometry('1230x700+100+10')
fake.attributes('-disabled',True)
fake.resizable(0,0)

#fakebackground
fakebg = ImageTk.PhotoImage(file='__img__\\background.jpg')
fbg = Label(fake,image=fakebg)
fbg.image=fakebg
fbg.pack()
#Background
background = ImageTk.PhotoImage(file='__img__\\avatar.png')
conform = ImageTk.PhotoImage(file='__img__\\next.png')

#Lable
bg = Label(root,image=background,bg='#fdfddb')
bg.image=background
bg.place(x=120,y=50)

#Entry
pascode = Entry(root,width=40,borderwidth=2,show='*')
#Include.tip(root,pascode,'Enter Password')
pascode.place(x=130,y=360)
pascode.focus()
Include.eye(root,pascode,x=380,y=360)

#Button
def check():
    from tkinter import messagebox
    password = pascode.get()
    if len(password) < 8 or len(password) > 32:
        messagebox.showerror('LOG-IN',' Ivalid password: Your password must contain 8 to 32 characters.')
    else:
        recived  = db.Password(password,'get')
        if recived[0] == recived[1]:
            fake.destroy()
            Rent()
        else:
            messagebox.showerror('LOG-IN',' Incorrect password.')
conf00 = Button(root,image=conform,borderwidth=0,bg='#fdfddb',command=check)
#Include.tip(root,conf00,'Confrom')
conf00.place(x=460,y=390)
root.mainloop()