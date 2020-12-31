from source import *
class Tree:

    def __init__(self,search_tree):
        self.frame = search_tree
        self.style = ttk.Style()

    def smallTree(self,*data):
        tv = ttk.Treeview(self.frame)

        self.style.configure(
            'Treeview',forground='#ffffff',
            fieldbackground="#ffffff",rowheight=20.3)
        self.style.map('Treeview',background=[('selected','#386ec3')])
        
        tv.tag_configure('strip1',background='#fffbff') 
        tv.tag_configure('strip2',background='#ebd8d0')

        tv['columns']=('Catagory','Amount')

        tv.column('#0',width=50,minwidth=25)
        tv.column('Catagory',anchor=CENTER,width=320)
        tv.column('Amount',anchor=W,width=120)

        tv.heading('#0',text='S.N',anchor=W)
        tv.heading('Catagory',text='Catagory',anchor=CENTER)
        tv.heading('Amount',text='Amount',anchor=W)
        headings = ['Electricity','Water','Waste','Rent','Total']
        for i in data:
            results = i[0][2:]
        numlist = [str(i)+'.' for i in range(1,(len(results)+1))]

        strip = None

        try:
            for i in range(len(results)):
                if i % 2 == 0:
                    strip = 'strip1'
                else:
                    strip = 'strip2'
                tv.insert(parent='',index='end',iid=i,text=numlist[i],value=(headings[i],results[i]),tags=(strip))
                tv.place(x=250,y=345,height=130,width=500)
        except IndexError:#HandelingAnUnknownError
            pass
        return tv
    
    def largeTree(self,*data):
        tv = ttk.Treeview(self.frame)

        self.style.configure(
            'Treeview',forground='#ffffff',
            fieldbackground="#ffffff",rowheight=20.3)
        self.style.map('Treeview',background=[('selected','#386ec3')])
        
        tv.tag_configure('strip1',background='#fffbff') 
        tv.tag_configure('strip2',background='#ebd8d0')

        tv['columns']=('Date of Record','Month','Electricity','Water',
        'Waste','Rent','Total')
        tv.column('#0',width=20,minwidth=25)
        tv.column('Date of Record',anchor=E,width=50)
        tv.column('Month',anchor=E,width=50)
        tv.column('Electricity',anchor=E,width=50)
        tv.column('Water',anchor=CENTER,width=50)
        tv.column('Waste',anchor=W,width=50)
        tv.column('Rent',anchor=W,width=50)
        tv.column('Total',anchor=W,width=50)

        tv.heading('#0',text='S.N',anchor=W)
        tv.heading('Date of Record',text='DOR',anchor=W)
        tv.heading('Month',text='Month',anchor=W)
        tv.heading('Electricity',text='Electricity',anchor=W)
        tv.heading('Water',text='Water',anchor=W)
        tv.heading('Waste',text='Waste',anchor=W)
        tv.heading('Rent',text='Rent',anchor=W)
        tv.heading('Total',text='Total',anchor=W)

        for i in data:
            results = i
        numlist = [str(i)+'.' for i in range(1,(len(results))+1)]

        strip = None
        try:
            for i in range(len(results)):
                if i % 2 == 0:
                    strip = 'strip1'
                else:
                    strip = 'strip2'
                tv.insert(parent='',index='end',iid=i,text=numlist[i],value=(results[i]),tags=(strip))
                tv.place(x=250,y=345,height=130,width=500)
        except IndexError:#HandelingAnUnknownError
            pass
        return tv