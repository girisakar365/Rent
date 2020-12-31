#**************************#
#__init__ (front-end)******#
#**************************#

from source import *
from db import db
from main import *
from Tree import Tree
from genPascode import *
# from search import Search
#WINDOW.CONFIGURE:
root = Tk()
root.attributes('-alpha',db.cache('fetch','alpha'))
root.title(' RENT')
root.iconbitmap('logo.ico')
root.geometry('1000x710+100+10')
root.resizable(0,0)

#IMAGES:
Avatar=Dp.image_loader(db.PhotoLib(1)[1])
LOGO = Dp.image_loader(db.PhotoLib(26)[1])
Change = Dp.image_loader(db.PhotoLib(3)[1])
Back = Dp.image_loader(db.PhotoLib(4)[1])
User = Dp.image_loader(db.PhotoLib(5)[1])
Electricity = Dp.image_loader(db.PhotoLib(6)[1])
Water = Dp.image_loader(db.PhotoLib(7)[1])
Garbage = Dp.image_loader(db.PhotoLib(8)[1])
Rent = Dp.image_loader(db.PhotoLib(9)[1])
Record = Dp.image_loader(db.PhotoLib(17)[1])
Search = Dp.image_loader(db.PhotoLib(11)[1])
Delete = Dp.image_loader(db.PhotoLib(12)[1])
Edit = Dp.image_loader(db.PhotoLib(13)[1])
Next = Dp.image_loader(db.PhotoLib(14)[1])
Chart = Dp.image_loader(db.PhotoLib(33)[1])
Clear = Dp.image_loader(db.PhotoLib(15)[1])
Scan = Dp.image_loader(db.PhotoLib(16)[1])
Reset = Dp.image_loader(db.PhotoLib(20)[1])
remove = Dp.image_loader(db.PhotoLib(24)[1])
Excel=Dp.image_loader(db.PhotoLib(32)[1])
rs = Dp.image_loader(db.PhotoLib(27)[1])
ss = Dp.image_loader(db.PhotoLib(28)[1])
ses =Dp.image_loader(db.PhotoLib(29)[1])
qr_code = Dp.image_loader(db.PhotoLib(30)[1])

def RENT():
    #TABS:
    Tabs = ttk.Notebook(root)
    Tabs.place(x=0,y=0)

    #FRAMES:
    Record_Section = Frame(Tabs,width=1230,height=700,bg=setbg.currentbg())
    Search_Section = Frame(Tabs,width=1230,height=700,bg=setbg.currentbg())
    Setting_Section = Frame(Tabs,width=1230,height=700,bg=setbg.currentbg())
    qr = Frame(Tabs,width=1230,height=700,bg=setbg.currentbg())

    Record_Section.pack(fill='both',expand=1)
    Search_Section.pack(fill='both',expand=1)
    Setting_Section.pack(fill='both',expand=1)
    qr.pack(fill='both',expand=1)

    Tabs.add(Record_Section,image=rs)
    Tabs.add(Search_Section,image=ss)
    Tabs.add(Setting_Section,image=ses)
    Tabs.add(qr,image=qr_code)
    Tabs.hide(3)

    style = ttk.Style()

    #RECORD-SECTION: 
    DCa = list(Include.digital_clock(Record_Section,x=5,y=40))

    Dp(fontSize=40)
    title1=Dp.text_label(Record_Section,'Record Section',x=290,y=125)
    Dp.reset_key()
    ele=Dp.image_label(win=Record_Section,image=Electricity,x=360,y=270)
    wa = Dp.image_label(win=Record_Section,image=Water,x=510,y=270)
    ws=Dp.image_label(win=Record_Section,image=Garbage,x=360,y=470)
    re = Dp.image_label(win=Record_Section,image=Rent,x=520,y=470)

    em1 = Dp.entry(Record_Section,x=330,y=330)
    em2 = Dp.entry(Record_Section,x=330,y=400)

    em2.focus()
    wm1 = Dp.entry(Record_Section,x=490,y=330)
    wm2 = Dp.entry(Record_Section,x=490,y=400)
    Dp(width=10)
    wc = Dp.entry(Record_Section,x=570,y=280)
    Dp.reset_key()
    waste = Dp.entry(Record_Section,x=330,y=530)
    rent = Dp.entry(Record_Section,x=490,y=530)

    Include.checkbox(Record_Section)
    style.configure('TCheckbutton',borderwith=0,
    background=setbg.currentbg(),
    activebackground=setbg.currentbg()
    ,font=('Bookman Old Style',8))

    clear_all = Dp.image_button(Record_Section,Clear,x=960,y=257)
    conform_record = Dp.image_button(Record_Section,Record,x=450,y=610)

    src = list(Include.combobox(win=Record_Section,x=730,y=365,z=820,p=365))
    mm = strftime('%B')
    yy=int(strftime('%Y'))
    src[0].current(src[2].index(mm))
    src[1].current(src[3].index(yy))

    wc.insert(0,200)
    waste.insert(0,175)
    rent.insert(0,14000)
    results=None
    try:
        for i in db.RS(src[1].get(),'fetch',strftime('%B')):
            results=i
        try:
            em1.insert(0,results[7])
            wm1.insert(0,results[8])
        except TypeError:
            pass
    except IndexError:
        pass

    #SEARCH-SECTION:
    DCb = list(Include.digital_clock(Search_Section,x=5,y=40))

    Dp(fontSize=40)
    title2 = Dp.text_label(Search_Section,'Search Section',x=290,y=125)
    Dp.reset_key()
    Dp(fontSize=12)
    no_record = Dp.text_label(Search_Section,text='Status: No Record',x=248,y=315)
    dor=Dp.text_label(Search_Section,text='Date Of Record:     None',x=480,y=315)    
    Dp.reset_key()

    ssc = list(Include.combobox(win=Search_Section,x=350,y=265,z=470,p=265))
 
    Dp(bg=setbg.currentbg())
    hide = Dp.text_label(Search_Section,'Please search your records.',x=30,y=345)
    hide['width']=75
    hide['height']=6

    search_record = Dp.image_button(Search_Section,Search,x=580,y=265)
    clear_table = Dp.image_button(Search_Section,Clear,x=960,y=257)
    delete_record = Dp.image_button(Search_Section,Delete,x=250,y=490)
    edit_record = Dp.image_button(Search_Section,Edit,x=310,y=490)
    qr_scan = Dp.image_button(Search_Section,Scan,x=370,y=490)
    chart=Dp.image_button(Search_Section,Chart,x=430,y=490)
    xls=Dp.image_button(Search_Section,Excel,x=500,y=490)
    
    delete_record.config(state='disabled')
    edit_record.config(state='disabled')
    qr_scan.config(state='disabled')
    chart.config(state='disabled')
    xls.config(state='disabled')

    #SETTINGS:
    DCc = list(Include.digital_clock(Setting_Section,x=5,y=40))
    Dp(fontSize=40)
    title3=Dp.text_label(Setting_Section,'Setting',x=390,y=125)
    Dp(fontSize=48)
    subtitle=Dp.text_label(Setting_Section,'Choose Options',x=257,y=277)
    Dp.reset_key()  

    Dp(bg='#c0c5ce')
    bar = Dp.text_label(Setting_Section,x=1,y=247)
    if db.cache('fetch','askpassword')=='enabled' and db.cache('fetch','password') !='empty':
        Security = Dp.image_loader(db.PhotoLib(2)[1])
    else:
        Security = Dp.image_loader(db.PhotoLib(25)[1])
    change_password = Dp.image_button(Setting_Section,Security,x=1,y=250)
    set_user = Dp.image_button(Setting_Section,User,x=1,y=300)
    change_background = Dp.image_button(Setting_Section,Change,x=1,y=350)
    back = Dp.image_button(Setting_Section,Back,x=1,y=400)
    Dp(bg=setbg.currentbg())
    reset = Dp.image_button(Setting_Section,Reset,x=960,y=135)

    bar['height'] = 7
    bar['bd'] = 20
    change_password['activebackground'] = '#c0c5ce'
    set_user['activebackground'] = '#c0c5ce'
    change_background['activebackground'] = '#c0c5ce'
    back['activebackground'] = '#c0c5ce'

    Dp.reset_key()

    #QR:
    DCd = list(Include.digital_clock(qr,x=5,y=40))
    Dp(fontSize=40)
    qrgen=Dp.text_label(qr,text='QR-CODE',x=370,y=125)
    Dp.reset_key()
    qr_info=Dp.text_label(qr,text='Please scan the QR-Code',x=380,y=575)

    hd=Dp.image_button(qr,remove,x=960,y=257)
    hd.config(command=lambda:[Tabs.hide(3),Tabs.select(0)])
    Tip(hd,'Clear QR-Code')


    #BALLOONS:
    Tip(ele,'Flat Electricity')
    Tip(wa,'Water Electricity')
    Tip(ws,'Waste')
    Tip(re,'Rent')
    Tip(em1,'Previous Meter')
    Tip(em2,'Present Meter')
    Tip(wm1,'Previous Meter')
    Tip(wm2,'Present Meter')
    Tip(wc,'Water Cost')
    Tip(waste,'Waste Cost')
    Tip(rent,'Rent Cost')
    Tip(clear_all,'Clear')

    Tip(conform_record,'Create Record')
    Tip(clear_table,'Clear Table')
    Tip(search_record,'Search')
    Tip(delete_record,'Delete Record')
    Tip(edit_record,'Edit Record')
    Tip(qr_scan,'Create QR Code')

    Tip(change_password,'Security')
    Tip(set_user,'User')
    Tip(change_background,'Customise Background')
    Tip(back,'Back')
    Tip(reset,'Reset to default')
    Tip(xls,'Export to excel')
    Tip(chart,'Chart')

    #Resetting:
    db.cache('meter',11)
    db.cache('cmd',False)
    db.cache('oid',None)

    #BACK-END:
    BE = BackEnd(
        clear_all,conform_record,search_record,edit_record,
        delete_record,qr_scan,clear_table,change_password,set_user
        ,change_background,back,reset,remove,hd,xls,chart,
        root=(root),
        tab=(Tabs),
        frame=(Record_Section,Search_Section,Setting_Section,qr),
        entries=(em1,em2,wm1,wm2,wc,waste,rent),
        style=(style),
        lables=(no_record,title1,title2,title3,ele,wa,ws,re,dor,qrgen,qr_info),
        DgC=(DCa,DCb,DCc,DCd),
        combo=(src,ssc)
        )

if db.cache('fetch','password')!='empty':

    root.config(bg=setbg.currentbg())
    user=Dp.image_label(root,Avatar,x=345,y=190)
    user.config(bg=setbg.currentbg())
    Dp(width=35)
    pascode = Dp.entry(root,x=370,y=490)
    pascode.focus()
    Include.eye(root,pascode,x=600,y=490)
    Tip(pascode,'Enter Password')
    conform = Dp.image_button(root,Next,x=960,y=660)
    
    def gate():
        if len(pascode.get()) == 0:
            Msg('Opps! You have not entered the password.','!')
        elif len(pascode.get())<8 or len(pascode.get())>32:
            Msg('Inappropriate password','!')
        else:
            if pascode.get() == Password.hexPassword(db.cache('fetch','password'),'decode'):
                RENT()
            else:
                Msg('Incorrect Password !','!')
    conform['command']=gate
    Tip(conform,'Conform')

else:
    RENT()
root.mainloop()