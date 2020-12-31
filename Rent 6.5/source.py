from db import db
from tkinter import*
from tkinter import ttk
from random import choice
from tkinter import messagebox
from time import strftime,sleep


#\defaultfunction\
def default():
    print('No function inserted!')

    
class setbg:
    def currentbg():
        bg = db.cache('fetch','bg')
        bg_dict = {
            '1': '#4f5bd5',	
            '2': '#fa7e1e',
            '3': '#ffdc73',
            '4':'#f04747',
            '5':'#2bc760',
            '6':'#d62976',
            '7':'#fce9db',
            '8':'#962fbf'
        }
        return bg_dict['{}'.format(bg)]
cbg = setbg.currentbg()

User = db.cache('fetch','user')
greetings = ['Hello','Hi','Welcome','Namaste']
greet = choice(greetings)

access = {
'bg':cbg,'atvbg':cbg,'fontSize':14,'fontStyle':'Bookman Old Style','fontType':'normal',
'x':0,'y':0,'width':20,'bd':1
}

class Dp:

    def __init__(self,**kwargs):
        for key,value in kwargs.items():                    
            access[key]=value
    
    def reset_key():
        defaults = {
        'bg':cbg,'fontSize':14,'fontStyle':'Bookman Old Style','fontType':'normal',
        'x':0,'y':0,'width':20,'bd':1}           
        for key,value in defaults.items():
            access[key]=value

    def text_label(win,text='',x=0,y=0):
        label = Label(win,text=text,bg=access['bg'],fg='#1d1f2a',font=(access['fontStyle'],access['fontSize'],access['fontType']))
        label.place(x=x,y=y)
        return label

    
    def image_label(win,image='',x=0,y=0):
        imglabel = Label(win,image=image,bg=access['bg'])
        imglabel.image = image
        imglabel.place(x=x,y=y)
        return imglabel

    def text_button(win,text='',x=0,y=0,func=default):
        button = Button(win,text=text,cursor="hand2",bg=access['bg'],font=(access['fontStyle'],access['fontSize'],access['fontType']),command=func,
        activebackground=access['atvbg'],bd=access['bd'])
        button.place(x=x,y=y)
        return button

    def image_button(win,image='',x=0,y=0,func=default):
        button = Button(win,cursor="hand2",image=image,bg=access['bg'],borderwidth=0,command=func,activebackground=access['bg'])
        button.image = image
        button.place(x=x,y=y)
        return button

    def entry(win,x=0,y=0):
        entry =ttk.Entry(win)
        entry.config(width=access['width'])
        entry.place(x=x,y=y)
        return entry
    
    def image_loader(imagename=''):
        from PIL import Image,ImageTk
        img = ImageTk.PhotoImage(data=imagename)
        return img

class Include:

    def conform(func,title,msg):
        def exe():
            get = messagebox.askyesno(title,msg)
            if get == True:
                try:
                    func()
                except TypeError:
                    pass
                return True
            else:
                pass
        return exe()

    def digital_clock(win,vartext=User,x=0,y=0):
        from time import strftime
        def clock():
            hour = strftime("%I")
            minute = strftime("%M")
            second = strftime("%S")
            am_pm = strftime('%p')
            day = strftime('%A, %B %d, %Y')
            digidate.config(text=day)
            digiclock.config(text=hour+':'+minute+':'+second+' '+am_pm)
            digiclock.after(1000,clock)
        digiclock = Dp.text_label(win,x=x,y=y)
        welcome_user = Dp.text_label(win,x=2,y=650,text='{}, {}'.format(greet,vartext))
        digidate = Dp.text_label(win,x=x+670,y=y)
        clock()
        return digiclock,digidate,welcome_user

    def combobox(win,x=0,y=0,z=0,p=0):
        s_00 = ['Month',
        'January','February','March','April','May','June',
        'July','August','September','October','November','December']

        s_01 = ['Year']
        start = 0
        for i in range(33):
            i = i+1
            start = 2019 + i
            s_01.append(int(start))
            
            #selectmonth
        month = ttk.Combobox(win,value=s_00,width=10)
        month.current(0)
        month.bind('<<ComboboxSelected>>')
        month.config(state='readonly')
        month.place(x=x,y=y)
            #selectyear
        year = ttk.Combobox(win,value=s_01,width=10)
        year.current(0)
        year.config(state='readonly')
        year.bind('<<ComboboxSelected>>')
        year.place(x=z,y=p)
        Tip(month,'Select Month')
        Tip(year,'Select Year')
        return month,year,s_00,s_01
    
    def checkbox(tab):
        hold = IntVar()
        hold.set('11')
        def meter():
            db.cache('meter',hold.get())
        u0 = ttk.Checkbutton(tab,cursor="hand2",text='11',variable=hold,onvalue=11,offvalue=0,command=meter)
        u1 = ttk.Checkbutton(tab,cursor="hand2",text='12',variable=hold,onvalue=12,offvalue=0,command=meter)
        u0.place(x=490,y=365)
        u1.place(x=530,y=365)
        Tip(u0,'Set unit to 11')
        Tip(u1,'Set unit to 12')
        return u0,u1,hold
    
    def slider(win,tab): 
        def change(x):
            db.cache('alpha',slide.get())
            win.attributes('-alpha',db.cache('fetch','alpha'))
            info.config(text=round(slide.get(),2))
        slide = ttk.Scale(tab,from_=0.1,to=1.0,value=(db.cache('fetch','alpha'))
            ,cursor='hand2',orient=VERTICAL,command=change)
        style=ttk.Style()
        style.configure('Vertical.TScale',background=setbg.currentbg(),activebackground=setbg.currentbg())
        slide.place(x=590,y=325)
        info=Dp.text_label(tab,text=round(db.cache('fetch','alpha'),2),x=615,y=360)
        info.config(bg=setbg.currentbg())
        Tip(slide,'Change tranparency of window')

    def eye(win,widget,x=0,y=0):       
        not_shown = Dp.image_loader(db.PhotoLib(18)[1])
        shown = Dp.image_loader(db.PhotoLib(19)[1])
        def unshow():
            s0 = Dp.image_button(win,not_shown,x=x,y=y)
            s0['command']=lambda:[show()]
            s0['activebackground']=access['bg']
            widget['show'] = '●'
            s0.place(x=x,y=y)
            Tip(s0,'show')

        def show():
            s1 = Dp.image_button(win,shown,x=x,y=y)
            s1['command']=lambda:[unshow()]
            s1['activebackground']=access['bg']
            widget['show'] = ''
            replace = widget.get()
            widget.delete(0,END)
            widget.insert(0,replace)
            s1.place(x=x,y=y)
            Tip(s1,'hide')
        unshow()
        return show,unshow

    def onoff(win,args,btw,function):
        toff = Dp.image_loader(db.PhotoLib(22)[1])
        ton = Dp.image_loader(db.PhotoLib(23)[1])
        lock = Dp.image_loader(db.PhotoLib(2)[1])
        unlock = Dp.image_loader(db.PhotoLib(25)[1])

        Dp(fontSize=8)
        status = Dp.text_label(win,text='',x=580,y=235)
        def off():
            onn=Dp.image_button(win,ton,x=540,y=235)
            status.config(text='Enabled')
            for i in range(len(args)):
                args[i].delete(0,END)
                args[i].config(state='normal')
            btw[0].config(state='normal')
            btw[1].config(image=lock)
            btw[2].config(state='normal')

            args[0].focus()
            onn.config(command=on)
            db.cache('askpassword','enabled')
            Tip(onn,'Disable security')
            
        def on():
            def subon():
                of=Dp.image_button(win,toff,x=540,y=235)
                status.config(text='Disabled')
                for i in range(len(args)):
                    args[i].delete(0,END)
                    args[i].config(state='disabled')
                for i in range(len(function)):
                    function[i][1]()
                of.config(command=off)
                db.cache('askpassword','disabled')
                btw[0].config(state='disabled')
                btw[1].config(image=unlock)
                btw[2].config(state='disabled')
                db.cache('password','empty')
                Tip(of,'Enable security')
            if db.cache('fetch','askpassword')=='disabled' or db.cache('fetch','password')=='empty':
                subon()
            elif db.cache('fetch','password')!='empty':
                conn=Include.conform(None,'RENT','Are your sure you want to disable security? Doing so will completely erase your password.')
                if conn == True:
                    subon()

        if db.cache('fetch','askpassword')=='enabled':
            if db.cache('fetch','password') =='empty':
                db.cache('askpassword','disabled')
                on()
            else:
                off()
        else:
            on()

class Tip(object):

    def __init__(self, widget, text='widget info'):
        self.waittime = 1500    #miliseconds
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
        x=y=0
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 30
        self.tw = Toplevel(self.widget)
        self.tw.attributes('-alpha',db.cache('fetch','alpha'))
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#f5f5f5",fg='#1d1f2a',relief='sunken', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

class Msg(object):
    def __init__(self,text,note='Note'):
        self.note=note
        self.text=text
        self.tw=None
        self.enter()
        from threading import Thread
        t1=Thread(target=self.leave)
        t1.start()

    def showtip(self):
        x =200
        y =530
        self.tw = Toplevel()
        self.tw.attributes('-alpha',db.cache('fetch','alpha'))
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        self.tw.attributes('-disabled',True)
        label = Label(self.tw, text='[{}] {}'.format(self.note,self.text), justify='left',
                       background="#fdeabc",fg='#1d1f2a',relief='sunken', borderwidth=1,
                       wraplength = 180)
        label.pack(ipadx=1)
    def enter(self):
        self.showtip()

    def leave(self,event=None):
        sleep(5)
        self.hide()

    def hide(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()