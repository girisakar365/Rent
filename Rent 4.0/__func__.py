from tkinter import *
from __bridge__ import *
from __dependency__ import Dp


#Function\Record_Section
#----------------------#

#Variables:
Meter = [11]

class RS:

    def meter(var):
        del Meter[0]
        Meter.append(var.get())  
    
    def confrom_record(acs,data,src,ssc):
        table = src[0].get()+'-'+src[1].get()
        month = src[0].get()

        condition = Operation.create_record(
            table,month,data[0],data[1],data[2],data[3],Meter[0],data[4],data[5],data[6]
        )

        if condition == False:
            pass
        else:
            data = db.dispaly_table(table)
            if data != False:
                acs[2].select(1)
                ssc[0].current(ssc[2].index(src[0].get()))
                ssc[1].current(ssc[3].index(int(src[1].get())))
                acs[1].config(text='Status:     Active')
                a=Dp.text_label(acs[0],text='Date Of Record: '+data[0],bg='#2c2f33',x=510,y=315,fontSize=10)
                a['fg']='#ffffff'
                SrS.displayTree(acs[0],data)
                acs[3]['state']='normal'
                acs[4]['state']='normal' 

    def clear(entries):
        for i in entries:
            i.delete(0,END)
        entries[1].focus()


#Function\Search_Section
#----------------------#

class SrS:

    def search(ssc,acs):
        data = db.dispaly_table(ssc[0].get()+'-'+ssc[1].get())
        if data != False:
            SrS.displayTree(acs[0],data)
            acs[1].config(text='Status:    Active')
            a=Dp.text_label(acs[0],text='Date Of Record: '+data[0],bg='#2c2f33',x=510,y=315,fontSize=10)
            a['fg']='#ffffff'
            acs[2]['state']='normal'
            acs[3]['state']='normal'

    def delete(ssc,lable):
        condtion = db.delete_table(ssc[0].get()+'-'+ssc[1].get())
        if condtion != False:
            lable.config(text='Status:    Deleted')


    def displayTree(win,data=[0,0,0,0,0,0,0]):
        tv = ttk.Treeview(win)

        tv['columns'] = ('Catagory','Amount')

        tv.column('#0',width=50,minwidth=25)
        tv.column('Catagory',anchor=CENTER,width=320)
        tv.column('Amount',anchor=W,width=120)
        tv.heading('#0',text='S.N',anchor=W)
        tv.heading('Catagory',text='Catagory',anchor=CENTER)
        tv.heading('Amount',text='Amount',anchor=W)

        results = data
        tv.insert(parent='',index='end',iid=0,text='1)',value=('Electricity',results[2]))
        tv.insert(parent='',index='end',iid=1,text='2)',value=('Water',results[3]))
        tv.insert(parent='',index='end',iid=2,text='3)',value=('Waste',results[4]))
        tv.insert(parent='',index='end',iid=3,text='4)',value=('Rent',results[5]))
        tv.insert(parent='',index='end',iid=4,text='5)',value=('Total Amount',results[6]))
        tv.place(x=250,y=345,height=130,width=500)
        return win

    def clear(win):
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
        SrS.displayTree(win[0])
        Dp.text_label(win[0],text='                                       ',x=510,y=315,bg=apply_bg)
        win[1].config(text='Status:     No Record')
        win[2][0].current(0)
        win[2][1].current(0)
        win[3].config(bg=apply_bg,activebackground=apply_bg)
        win[4].config(bg=apply_bg)
        if apply_bg == '#ff0000':
            win[4].config(activebackground='#ffa8a3')
        else:
            win[4].config(activebackground='#ff0000')
        win[3]['state']='disabled'
        win[4]['state']='disabled'

class StS:

    def change_password(pp,np,rnp):
        from tkinter import messagebox
        conditon = messagebox.askyesno('Security','Are you sure you want to change your password?')
        if conditon == True:
            conn = Operation.renew(pp,np,rnp)
            if conn == True:
                messagebox.showinfo('Security','Password successfully changed.')
    
    def user(user):
        conn = db.cache2(user[0],'insert')
        if conn == False:
            pass
        else:
            a=db.cache2(0,'get')
            user[1].config(text='User: '+a)
            user[2].config(text='User: '+a)
            user[3].config(text='User: '+a)