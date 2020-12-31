from tkinter import *
from tkinter import ttk
from time import strftime

from __dependency__ import *
from db import db
from __func__ import *

#MainWindow
root = Tk()
root.attributes('-alpha',0.95)
root.title(' RENT')
root.iconbitmap('__img__\\logo.ico')
root.geometry('1000x700+100+10')
root.resizable(0,0)

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

user = db.cache2(0,'get')
if user == False:
    user = 'Admin'

#LoadImage
    #icon_image
avatar = Dp.image_loader('__img__\\avatar.png')
Security = Dp.image_loader('__img__\\change_password.ico')
Change = Dp.image_loader('__img__\\change_background.png')
Back = Dp.image_loader('__img__\\left-arrow.png')
User = Dp.image_loader('__img__\\man.png')
Electricity = Dp.image_loader('__img__\\electric-meter.png')
Water = Dp.image_loader('__img__\\water_meter.png')
Garbage = Dp.image_loader('__img__\\garbage.png')
Rent = Dp.image_loader('__img__\\real-estate.png')
Record = Dp.image_loader('__img__\\record.ico')
Search = Dp.image_loader('__img__\\search.png')
Delete = Dp.image_loader('__img__\\delete_record.ico')
Edit = Dp.image_loader('__img__\\edit_record.ico')
Next = Dp.image_loader('__img__\\next.png')
Clear = Dp.image_loader('__img__\\backspace.png')

#Colours
yellow = '#fdfddb'
gray_white = '#cecece'
pure_white = '#f2d000'
red = '#ff0000'
blue = '#143d8c'
green = '#2bc760'

def RENT():
    #Tabs\Notebook\ttk
    Tabs = ttk.Notebook(root)
    Tabs.place(x=0,y=0)

    #Frames
    Record_Section = Frame(Tabs,width=1230,height=700,bg=apply_bg)
    Record_Section.pack(fill='both',expand=1)
    Search_Section = Frame(Tabs,width=1230,height=700,bg=apply_bg)
    Search_Section.pack(fill='both',expand=1)
    Setting_Section = Frame(Tabs,width=1230,height=700,bg=apply_bg)
    Setting_Section.pack(fill='both',expand=1)
    Tabs.add(Record_Section,text='  Record Section  ')
    Tabs.add(Search_Section,text='  Search Section  ')
    Tabs.add(Setting_Section,text='     Setting     ')
    style = ttk.Style()




                ###__Record_Section__###
    #DigitalClock
    DCa = list(Include.digital_clock(Record_Section,x=5,y=40))
    DCa[2].config(text='User: '+user)

        #LabelsInFrame
    title1=Dp.text_label(Record_Section,'Record Section',fontSize=40,x=290,y=125)
    ele=Dp.image_label(win=Record_Section,image=Electricity,x=360,y=270)
    Tip(ele,'Flat Electricity')
    wa = Dp.image_label(win=Record_Section,image=Water,x=510,y=270)
    Tip(wa,'Water Electricity')
    ws=Dp.image_label(win=Record_Section,image=Garbage,x=360,y=470)
    Tip(ws,'Waste')
    re = Dp.image_label(win=Record_Section,image=Rent,x=510,y=470)
    Tip(re,'Rent')

        #EntriesInFrame
    em1 = Dp.entry(Record_Section,x=330,y=330)
    Tip(em1,'Previous Meter')
    em2 = Dp.entry(Record_Section,x=330,y=400)
    Tip(em2,'Present Meter')
    em2.focus()
    wm1 = Dp.entry(Record_Section,x=490,y=330)
    Tip(wm1,'Previous Meter')

    #CheckBox
    hold = IntVar()
    hold.set('11')
    u0 = ttk.Checkbutton(Record_Section, text='11',variable=hold,onvalue=11,offvalue=0,command=lambda:[RS.meter(hold)])
    u1 = ttk.Checkbutton(Record_Section,text='12',variable=hold,onvalue=12,offvalue=0,command=lambda:[RS.meter(hold)])
    style.configure('TCheckbutton',borderwith=0,background=apply_bg,activebackground=apply_bg
    ,font=('Bookman Old Style',8))
    u0.place(x=490,y=365)
    u1.place(x=530,y=365)
    Tip(u0,'Unit')
    Tip(u1,'Unit')

    wm2 = Dp.entry(Record_Section,x=490,y=400)
    Tip(wm2,'Present Meter')
    wc = Dp.entry(Record_Section,x=570,y=280,width=10)
    Tip(wc,'Water Cost')
    waste = Dp.entry(Record_Section,x=330,y=530)
    Tip(waste,'Waste Cost')
    rent = Dp.entry(Record_Section,x=490,y=530)
    Tip(rent,'Rent Cost')

    #ComboBox1
    src = list(Include.combobox(win=Record_Section,x=750,y=265,z=840,p=265))
    mm = strftime('%B')
    yy=int(strftime('%Y'))
    src[0].current(src[2].index(mm))
    src[1].current(src[3].index(yy))

    #Button
    clear_all = Dp.image_button(Record_Section,Clear,x=960,y=257)
    Tip(clear_all,'Clear')
    clear_all['command']=lambda:[RS.clear([em1,em2,wm1,wm2,wc,waste,rent])]
    conform_record = Dp.image_button(Record_Section,Record,x=450,y=610)
    conform_record['command']=lambda:[RS.confrom_record([Search_Section,no_record,Tabs,delete_record,edit_record],
        [em2.get(),em1.get(),wm2.get(),wm1.get(),wc.get(),waste.get(),rent.get()],src,ssc
    )]
    Tip(conform_record,'Create Record')




                ###__Search_Section__###

    #DigitalClock
    DCb = list(Include.digital_clock(Search_Section,x=5,y=40))
    DCb[2].config(text='User: '+user)

        #LabelsInFrame
    title2 = Dp.text_label(Search_Section,'Search Section',fontSize=40,x=290,y=125)
    global no_record
    no_record = Dp.text_label(Search_Section,text='Status:     No Record',fontSize=12,x=248,y=315)    
    #ComboBox2
    global ssc
    ssc = list(Include.combobox(win=Search_Section,x=350,y=265,z=470,p=265))

    SrS.displayTree(Search_Section)

    #Button
    search_record = Dp.image_button(Search_Section,Search,x=580,y=265)
    search_record['command']=lambda: [SrS.search(ssc,[Search_Section,no_record,delete_record,edit_record])]
    Tip(search_record,'Search')

    clear_table = Dp.image_button(Search_Section,Clear,x=960,y=257)
    clear_table['command']=lambda:[SrS.clear([Search_Section,no_record,ssc,delete_record,edit_record])]
    Tip(clear_table,'Clear Table')

    global delete_record
    delete_record = Dp.image_button(Search_Section,Delete,x=250,y=490)
    delete_record['state']='disabled'
    delete_record['command']=lambda:[SrS.delete(ssc,no_record),edit_record.config(state='disabled')]
    Tip(delete_record,'Delete Record')

    if apply_bg == '#ff0000':
        delete_record['activebackground'] = '#ffa8a3'
    else:
        delete_record['activebackground'] = 'red'

    global edit_record
    edit_record = Dp.image_button(Search_Section,Edit,x=310,y=490)
    Tip(edit_record,'Edit Record')
    edit_record['state']='disabled'
    edit_record['command']=lambda:[Tabs.select(0)]

    
    
    
                    ###__Setting_Section__###
    #Labels
    DCc = list(Include.digital_clock(Setting_Section,x=5,y=40))
    DCc[2].config(text='User: '+user)
    title3=Dp.text_label(Setting_Section,'Setting',fontSize=40,x=390,y=125)
    subtitle=Dp.text_label(Setting_Section,'Choose Options',fontSize=48,x=257,y=277)
    bar = Dp.text_label(Setting_Section,bg='#c0c5ce',x=1,y=247)
    bar['height'] = 7
    bar['bd'] = 20

    class setting:

        def current_background():#UpdateBackground
            bg = db.cache(0,'get')
            return bg_dict['{}'.format(bg)]
        
        def hide():#hideandshowUpdate
            bg = setting.current_background()
            a = Dp.text_label(Setting_Section,x=220,y=190)
            a['bd'] = 550
            a.config(bg=bg)
            
        def password_change():#Chnage_password
            # Lables
            apply_bg2 = setting.current_background()
            setting.hide()
            Title = Dp.text_label(Setting_Section,text='  Security',fontSize=20,x=390,y=225,fontType='italic')
            Title.config(bg=apply_bg2)
            subhead1 = Dp.text_label(Setting_Section,text='Current Password',fontType='italic',x=380,y=285)
            subhead1.config(bg=apply_bg2)
            subhead2 = Dp.text_label(Setting_Section,text='New Password',fontType='italic',x=380,y=365)
            subhead2.config(bg=apply_bg2)
            subhead3 = Dp.text_label(Setting_Section,text='Re-Enter Password',fontType='italic',x=380,y=445)
            subhead3.config(bg=apply_bg2)

            #Entries
            current_password = Dp.entry(Setting_Section,x=380,y=330,width=30)
            current_password.focus()
            Include.eye(Setting_Section,current_password,x=580,y=330,bg=apply_bg2)
            new_password = Dp.entry(Setting_Section,x=380,y=400,width=30)
            Include.eye(Setting_Section,new_password,x=580,y=400,bg=apply_bg2)
            re_password = Dp.entry(Setting_Section,x=380,y=485,width=30)
            Include.eye(Setting_Section,re_password,x=580,y=485,bg=apply_bg2)

            #Button
            change = Dp.image_button(Setting_Section,Next,x=600,y=550)
            change.config(bg=apply_bg2,activebackground=apply_bg2)
            change['command']=lambda:[StS.change_password(current_password.get(),new_password.get(),re_password.get())]

        def user_set():#Set_user
            apply_bg2 = setting.current_background()
            setting.hide()
            #Lable
            subhead1 = Dp.text_label(Setting_Section,text='User Name',fontSize=20,x=410,y=255,fontType='italic')
            subhead2 = Dp.text_label(Setting_Section,text=' What should I call you ?',x=370,y=325)
            subhead1.config(bg=apply_bg2)
            subhead2.config(bg=apply_bg2)
            #Entry
            user = Dp.entry(Setting_Section,width=30,x=390,y=365,bd=0)
            user['bg'] = apply_bg2
            user['fg'] = '#313035'
            user['font'] = ('Bookman Old Style',16,'italic')
            user.focus()

            #Button 
            change = Dp.image_button(Setting_Section,Next,x=545,y=405)
            change.config(bg=apply_bg2,activebackground=apply_bg2)
            change['command']=lambda:[StS.user([user.get(),DCa[2],DCb[2],DCc[2]])]

        def bg_change():#Bg_change\Reveser
            apply_bg2 = setting.current_background()
            setting.hide()
            
            #Lables:
            b = Dp.text_label(Setting_Section,x=300,y=320,bg='#2c2f33')
            b['width']=23
            b['height']=5
            subhead1=Dp.text_label(Setting_Section,text='Customize Backgound',fontSize=20,x=300,y=225,fontType='italic')
            subhead2=Dp.text_label(Setting_Section,text='Select Colour:',fontSize=14,x=320,y=302,fontType='italic')
            subhead1.config(bg=apply_bg2)
            subhead2.config(bg=apply_bg2)

            #Buttons:
            def color(bg_num):
                if bg_num == 1:
                    db.cache(1,'insert')
                elif bg_num == 2:
                    db.cache(2,'insert')
                elif bg_num == 3:
                    db.cache(3,'insert')
                elif bg_num == 4:
                    db.cache(4,'insert')
                elif bg_num == 5:
                    db.cache(5,'insert')
                elif bg_num == 6:
                    db.cache(6,'insert')
                elif bg_num == 7:
                    db.cache(7,'insert')
                elif bg_num == 8:
                    db.cache(8,'insert')
                Update.refresh()

            ye = Dp.text_button(Setting_Section,text='      ',bg=yellow,x=320,y=340)
            ye['command']=lambda:[color(1),setting.reverse()]
            ye['borderwidth'] = 0
            ye['activebackground']=yellow
            w = Dp.text_button(Setting_Section,text='      ',bg=gray_white,x=390,y=340)
            w['borderwidth'] = 0
            w['activebackground']=gray_white
            w['command']=lambda:[color(2),setting.reverse()]
            wh = Dp.text_button(Setting_Section,text='      ',bg=pure_white,x=460,y=340)
            wh['borderwidth'] = 0
            wh['activebackground']=pure_white
            wh['command']=lambda:[color(3),setting.reverse()]
            re = Dp.text_button(Setting_Section,text='      ',bg=red,x=530,y=340)
            re['borderwidth'] = 0
            re['activebackground']=red
            re['command']=lambda:[color(4),setting.reverse()]

            gr = Dp.text_button(Setting_Section,text='      ',bg=green,x=320,y=390)
            gr['borderwidth'] = 0
            gr['activebackground']=green
            gr['command']=lambda:[color(5),setting.reverse()]
            gw = Dp.text_button(Setting_Section,text='      ',bg=blue,x=390,y=390)
            gw['borderwidth'] = 0
            gw['activebackground']=blue
            gw['command']=lambda:[color(6),setting.reverse()]
            bl = Dp.text_button(Setting_Section,text='      ',bg='#8abadb',x=460,y=390)
            bl['borderwidth'] = 0
            bl['activebackground']='#8abadb'
            bl['command']=lambda:[color(7),setting.reverse()]
            pr = Dp.text_button(Setting_Section,text='      ',bg='#936cca',x=530,y=390)
            pr['borderwidth'] = 0
            pr['activebackground']='#936cca'
            pr['command']=lambda:[color(8),setting.reverse()]

            Tip(ye,'Cream')
            Tip(w,'Gray White')
            Tip(wh,'Golden Yellow')
            Tip(re,'Tomato Red')
            Tip(gr,'Green')
            Tip(gw,'Dark Blue')
            Tip(bl,'Light Blue')
            Tip(pr,'Purple')
        
        def reverse():#Reverse\switch_1
            apply_bg2 = setting.current_background()
            setting.hide()
            setting.bg_change()
            SrS.clear([Search_Section,no_record,ssc,edit_record,delete_record])
        

        def go_back():#Go_back\Back
            apply_bg2 = setting.current_background()
            setting.hide()
            subtitle=Dp.text_label(Setting_Section,'Choose Options',fontSize=48,x=257,y=277)
            subtitle.config(bg=apply_bg2)

    change_password = Dp.image_button(Setting_Section,Security,x=1,y=250,bg='#c0c5ce')
    Tip(change_password,'Security')
    change_password['command'] = lambda:[setting.password_change()]
    change_password['activebackground'] = '#c0c5ce'
    set_user = Dp.image_button(Setting_Section,User,x=1,y=300,bg='#c0c5ce')
    set_user['command'] = lambda:[setting.user_set()]
    Tip(set_user,'User')
    set_user['activebackground'] = '#c0c5ce'
    change_background = Dp.image_button(Setting_Section,Change,x=1,y=350,bg='#c0c5ce')
    Tip(change_background,'Customise Background')
    change_background['command'] = lambda:[setting.bg_change()]
    change_background['activebackground'] = '#c0c5ce'
    back = Dp.image_button(Setting_Section,Back,x=1,y=400,bg='#c0c5ce')
    Tip(back,'Back')
    back['command'] = lambda:[setting.go_back(),Tabs.select(0)]
    back['activebackground'] = '#c0c5ce'




    class Update:

        def refresh():
            
            bg = db.cache(0,'get')
            apply_bg = bg_dict['{}'.format(bg)]
            
            #LabelsConfig
            DCa[0].config(bg=apply_bg)
            DCa[1].config(bg=apply_bg)
            DCa[2].config(bg=apply_bg)
            DCb[0].config(bg=apply_bg)
            DCb[1].config(bg=apply_bg)
            DCb[2].config(bg=apply_bg)
            DCc[0].config(bg=apply_bg)
            DCc[1].config(bg=apply_bg)
            DCc[2].config(bg=apply_bg)

            Record_Section.config(bg=apply_bg)
            title1.config(bg=apply_bg)
            ele.config(bg=apply_bg)
            wa.config(bg=apply_bg)
            ws.config(bg=apply_bg)
            re.config(bg=apply_bg)
            conform_record.config(bg=apply_bg,activebackground=apply_bg)
            style.configure('TCheckbutton',borderwith=0,background=apply_bg,activebackground=apply_bg,font=('Bookman Old Style',8))
            clear_all.config(bg=apply_bg,activebackground=apply_bg)

            Search_Section.config(bg=apply_bg)
            title2.config(bg=apply_bg)
            no_record.config(bg=apply_bg)
            edit_record.config(bg=apply_bg,activebackground=apply_bg)
            delete_record.config(bg=apply_bg)
            if apply_bg == '#ff0000':
                delete_record.config(activebackground='#ffa8a3')
            else:
                delete_record.config(activebackground='#ff0000')
            search_record.config(bg=apply_bg,activebackground=apply_bg)
            clear_table.config(bg=apply_bg,activebackground=apply_bg)

            Setting_Section.config(bg=apply_bg)
            title3.config(bg=apply_bg)
            subtitle.config(bg=apply_bg)            

#Entry:
root.config(bg=apply_bg)
Avatar = Dp.image_label(root,avatar,x=345,y=190)
Avatar.config(bg=apply_bg)

def start(pascode):
    condition = Operation.log(pascode)
    if condition == True:
        RENT()
pascode = Dp.entry(root,width=40,x=350,y=490)
pascode.focus()
Include.eye(root,pascode,x=600,y=490)
Tip(pascode,'Enter Password')
conform = Dp.image_button(root,Next,x=960,y=660)
conform['command']=lambda:[start(pascode)]
root.mainloop()