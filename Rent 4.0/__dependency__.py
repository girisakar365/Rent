from tkinter import *
from tkinter import messagebox

from db import db


bg = db.cache(0,'get')
bg_dict = {
    '1': '#fdfddb',
    '2': '#cecece',
    '3': '#f2d000',
    '4':'#ff0000',
    '5':'#2bc760',
    '6':'#143d8c',
    '7':'#8abadb',
    '8':'#936cca'
}
apply_bg = bg_dict['{}'.format(bg)]

#\defaultfunction\
def default():
    print('No function inserted!')

class Dp:

    def text_label(win,text='',bg=apply_bg,fontSize=14,fontStyle='Bookman Old Style',fontType='normal',x=0,y=0):
        label = Label(win,text=text,bg=bg,font=(fontStyle,fontSize,fontType))
        label.place(x=x,y=y)
        return label
    
    def image_label(win,image='',x=0,y=0,bg=apply_bg):
        imglabel = Label(win,image=image,bg=bg)
        imglabel.image = image
        imglabel.place(x=x,y=y)
        return imglabel

    def text_button(win,text='',bg=apply_bg,fontSize=10,fontStyle='Bookman Old Style',fontType='normal',x=0,y=0,func=default):
        button = Button(win,text=text,bg=bg,font=(fontStyle,fontSize,fontType),command=func)
        button.place(x=x,y=y)
        return button

    def image_button(win,image='',x=0,y=0,bg=apply_bg,func=default):
        button = Button(win,image=image,bg=bg,borderwidth=0,command=func,activebackground=bg)
        button.image = image
        button.place(x=x,y=y)
        return button

    def entry(win,width=20,bd=1.5,x=0,y=0):
        entry = Entry(win,width=width,borderwidth=bd)
        entry.place(x=x,y=y)
        return entry
    
    def image_loader(imagename=''):
        from PIL import Image,ImageTk
        img = ImageTk.PhotoImage(file=imagename)
        return img

class Include:

    def digital_clock(win,vartext='Admin',x=0,y=0):
        from time import strftime
        def clock():
            hour = strftime("%I")
            minute = strftime("%M")
            second = strftime("%S")
            am_pm = strftime('%p')
            day = strftime('%d-%B-%Y   %A')
            digidate.config(text=day)
            digiclock.config(text=hour+':'+minute+':'+second+' '+am_pm)
            digiclock.after(1000,clock)
        digiclock = Dp.text_label(win,x=x,y=y)
        #Include.tip(win,digiclock,'Time')
        welcome_user = Dp.text_label(win,x=2,y=650,text='User: {}'.format(vartext))
        digidate = Dp.text_label(win,x=x+700,y=y)
        #Include.tip(win,digidate,'Date')
        clock()
        return digiclock,digidate,welcome_user

    def conform(func,title,msg):
        get = messagebox.askyesno(title,msg)
        if get == True:
            func()
            return True
        else:
            pass

    def combobox(win,x=0,y=0,z=0,p=0):
        s_00 = ['Month',
        'January','February','March','April','May','June',
        'July','August','September','October','November','December']

        s_01 = ['Year']
        start = 0
        for i in range(33):
            i = i+1
            start = 2019 + i
            s_01.append(start)

            #selectmonth
        month = ttk.Combobox(win,value=s_00,width=10)
        month.current(0)
        month.bind('<<ComboboxSelected>>')
        month.config(state='readonly')
        Tip(month,'Select Month')
        month.place(x=x,y=y)
            #selectyear
        year = ttk.Combobox(win,value=s_01,width=10)
        year.current(0)
        year.config(state='readonly')
        year.bind('<<ComboboxSelected>>')
        Tip(year,'Select Year')
        year.place(x=z,y=p)
        return month,year,s_00,s_01

    def eye(win,widget,x=0,y=0,bg=apply_bg):
        
        not_shown = Dp.image_loader('__img__\\nshow.png')
        shown = Dp.image_loader('__img__\\show.png')

        def unshow():
            s0 = Dp.image_button(win,not_shown,x=x,y=y,bg=bg)
            s0['command']=lambda:[show()]
            s0['activebackground']=bg
            widget['show'] = '●'
            #Include.tip(win,widget,'Show')
            s0.place(x=x,y=y)

        def show():
            s1 = Dp.image_button(win,shown,x=x,y=y,bg=bg)
            s1['command']=lambda:[unshow()]
            s1['activebackground']=bg
            widget['show'] = ''
            replace = widget.get()
            widget.delete(0,END)
            widget.insert(0,replace)
            #Include.tip(win,widget,'Unshow')
            s1.place(x=x,y=y)
        unshow()


class Tip(object):

    def __init__(self, widget, text='widget info'):
        self.waittime = 1000     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.unschedule()
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id) 

    def showtip(self, event=None):
        x = y = 0
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 25
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#eeeac4", relief='raised', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()