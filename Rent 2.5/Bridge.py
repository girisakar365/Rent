#__BUILD-IN's__#
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import date

#Selfmodule#
from db import db

class Include:

    def digital_clock(win,x=0,y=0):
        from time import strftime
        def clock():
            hour = strftime("%I")
            minute = strftime("%M")
            second = strftime("%S")
            am_pm = strftime('%p')
            day = strftime('%d - %B - %Y  %A')
            digidate.config(text=day)
            digiclock.config(text=hour+' : '+minute+' : '+second+' '+am_pm)
            digiclock.after(1000,clock)
        digiclock = Label(win,text='',font=('Bookman Old Style',18,'normal'),bg='#fdfddb')
        digiclock.place(x=x,y=y)
        #Include.tip(win,digiclock,'Time')
        digidate = Label(win,text='',font=('Bookman Old Style',18,'normal'),bg='#fdfddb')
        #Include.tip(win,digidate,'Date')
        digidate.place(x=x+380,y=y)
        clock()

    def txt(win,text='',bg='#fdfddb',fontSize=14,fontStyle='Bookman Old Style',fontType='normal',x=0,y=0):
        a = Label(win,text=text,bg=bg,font=(fontStyle,fontSize,fontType))
        a.place(x=x,y=y)
    
    def eye(win,widget,x=0,y=0,bg='#fdfddb'):
        def unshow():
            not_shown = ImageTk.PhotoImage(file='__img__\\nshow.png')
            a = Button(win,image=not_shown,borderwidth=0,bg=bg,command=show)
            a.image = not_shown
            a.place(x=x,y=y)
            widget['show'] = '*'
            #Include.tip(win,widget,'Show')

        def show():
            shown = ImageTk.PhotoImage(file='__img__\\show.png')
            a = Button(win,image=shown,borderwidth=0,bg=bg,command = unshow)
            a.image = shown
            widget['show'] = ''
            b = widget.get()
            widget.delete(0,END)
            widget.insert(0,b)
            #Include.tip(win,widget,'Unshow')
            a.place(x=x,y=y)
    
        unshow()

    def conform(win,func,title,msg):
        get = messagebox.askyesno(title,msg,parent=win)
        if get == True:
            func()
        else:
            pass

class OAJ:

    def create_record(table,e_now,e_previous,w_now,w_previous,meter,water,waste,rent):
        
        def calculation():
        	#calculation
            a = int(e_now) - int(e_previous)
            b = int(w_now) - int(w_previous)
            c = b/2
            d = a + c
            e = d*int(meter)
            print(e)
            return e
        
        def store():
            #store    
            from datetime import date
            time = date.today()
            splittime = time.strftime('%a-%b-%Y')
            electricity = calculation()
            Total = electricity+int(water)+int(waste)+int(rent)
            raw = [splittime,electricity,water,waste,rent,Total]
            db.insert_data(table,raw)

        def check_gate():
            #Check
            condition = [
                len(str(e_now)) == 0,
                len(str(w_now)) == 0,
                len(str(e_previous)) == 0,
                len(str(w_previous)) == 0,
                len(str(water)) == 0,
                len(str(waste)) == 0,
                len(str(rent)) ==  0
            ]

            if any(condition):
                messagebox.showerror('Error: 411.1','Entries are Incomplete.')
                return False
            else:
                try:
                    int(e_now)
                    int(e_previous)
                    int(w_now)
                    int(w_previous)
                    int(water)
                    int(waste)
                    int(rent)
                except ValueError:
                    messagebox.showerror('Error: 411.2','Invalid value: Your data must be NUMBERS NOT ALPHABATES')
                    return False
                else:
                    store()
                    return True
        condition = check_gate()
        return condition
        
    def renew(win,pp,np,rnp):
        #check
        recieve = list(db.Password(pp,'get'))
        if recieve[0] == recieve[1]:
            if np == rnp:
                db.Password(rnp,'renew')
            else:
                messagebox.showerror('Security','Your password(s) did not match.',parent=win)
        else:
            messagebox.showerror('Security','Incorrect (Current) Password.',parent=win)