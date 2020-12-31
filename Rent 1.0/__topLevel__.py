from tkinter import *
import __mainData__
def Ui03():
#Ui_setup 
    ui3 = Toplevel()

    #Basics
    ui3.title('Record') 
    ui3.geometry('400x400+500+100')
    ui3.iconbitmap('__img__\\logo.ico')
    ui3.resizable(0,0)
    ui3.configure(bg='#3b93e7')

    #Entries
    search_entry = Entry(ui3,width=35,borderwidth=3,bg='#ffffff')
    search_entry.place(x=100,y=60)

    def main_func(data):
        display = ttk.Treeview(ui3)

        display['columns'] = ('Catagory','Amount')
        
        display.column('#0',width=0,minwidth=25)
        display.column('Catagory',anchor=CENTER,width=120)
        display.column('Amount',anchor=W,width=120)

        display.heading('#0',text='S.N',anchor=W)
        display.heading('Catagory',text='Catagory',anchor=CENTER)
        display.heading('Amount',text='Amount',anchor=W)

        results = list(data)
        display.insert(parent='',index='end',iid=0,text='1)',value=('Electricity',results[1]))
        display.insert(parent='',index='end',iid=1,text='2)',value=('Water',results[2]))
        display.insert(parent='',index='end',iid=2,text='3)',value=('Waste',results[3]))
        display.insert(parent='',index='end',iid=3,text='4)',value=('Rent',results[4]))
        display.insert(parent='',index='end',iid=4,text='5)',value=('Total',results[5]))
        display.place(x=0,y=170,height=160,width=500)
        
        date = Label(ui3,text=results[0],bg='#3b93e7',
        font=('time new roman',11,'bold')).place(x=100,y=140)
        delete = Button(
            ui3,text='Remove Data',command=lambda: [__mainData__.delete_record(search_entry.get())]
        ).place(x=0,y=140)
        

    def connector():
        
        data00 = __mainData__.display_db00(search_entry.get())
        
        if data00 == False:
            messagebox.showerror('Error','Record not found!')

        else:
            main_func(data00)
    #Button
    record_search = Button(ui3,text='Search',command=lambda: [connector()]).place(x=325,y=55)
#Ui03()