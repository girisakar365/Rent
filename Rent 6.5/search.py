"""
__File__: search tab
Source of import:  main
Buttons import: Clear,Search,Delete,Edit,QR
Lable import: no_record,dor
combo import: src
"""

from Tree import Tree
from db import db
from source import *
from tkinter import filedialog
from csv import writer,reader

class Search:
    def __init__(self,*args,**kwargs):

        self.tool={key:value for key,value in kwargs.items()}
        
        self.frame=self.tool['frame']
        self.clear = args[0]
        self.search = args[1]
        self.delete = args[2]
        self.edit = args[3]
        self.qr = args[4]
        self.xls=args[5]
        self.chart=args[6]

        self.today = strftime('%d/%m/%Y')

        self.data=None
        self.type=None
        self.qrdata=None
        self.tree=None

        self.combo = self.tool['combo']
        self.zombo=self.tool['zombo']
        self._Tree=Tree(self.frame)

        self.xls['command']=self._xls
        self.search['command']=self._search
        self.clear['command']=self._clear
        self.delete['command']=self._delete
        self.chart['command']=self._chart
        self.edit['command']=self._edit
        self.qr['command']=self._qr

    
    def endisable(self,status,DoR,state):
        self.tool['lables'][0].config(text='Status: {}'.format(status)) #Lable:No_Record
        self.tool['lables'][1].config(text='Date Of Record:     {}'.format(DoR))#Lable:dor
        self.edit.config(state=state)
        self.delete.config(state=state)
        self.qr.config(state=state)
        self.xls.config(state=state)
        self.chart.config(state=state)
    
    def _clear(self,text='Please search your records.'):
        self.combo[0].current(0)
        self.combo[1].current(0)
        self.endisable('No Record','None','disabled')
        Dp(bg=setbg.currentbg())
        hide = Dp.text_label(self.frame,text,x=30,y=345)
        hide['width']=75
        hide['height']=6

    def _search(self):
        if self.combo[0].get()=='Month' and self.combo[1].get()!='Year':
            self.endisable('Active',self.today,'normal')
            data = db.RS(self.combo[1].get(),'fetchall')

            if len(data)==0:
                self._clear(self.combo[1].get()+' do not contain any record.')
            self.type='large'
            self.tree = self._Tree.largeTree(data)
        
        elif self.combo[1].get()=='Year':
            self._clear('Please select a proper month or record to find your record.')

        else:
            data=db.RS(self.combo[1].get(),'fetch',self.combo[0].get())
            if len(data)>1:
                self.endisable('Active',self.today,'normal')
                self.type='large'
                self.tree=self._Tree.largeTree(data)
                
            elif len(data)==1:
                self.endisable('Active',self.today,'normal')
                self.type='small'
                self.data=data[0]
                self.tree=self._Tree.smallTree(data)
            
            elif len(data)==0:
                self._clear('Opps! The record your searched was not found.')

    def _delete(self):
        if self.type=='large':
            try:
                db.RS(self.combo[1].get(),'delete',self.tree.item(self.tree.selection())['values'][-1])
                self._search()
            except IndexError:
                Msg('Please select the record first.','!')     
        elif self.type=='small':
            db.RS(self.combo[1].get(),'delete',self.data[-1])
            self._search()
    
    def _edit(self):
        if self.type=='large':

            data=self.tree.item(self.tree.selection())['values'][3:]

        elif self.type=='small':
            data=self.data[3:]

        if len(data)==0:
            Msg('Select your record frist','!')
        else:
            self.tool['tab'].select(0)
            get=[]
            get.append(data[6])
            get.append(data[4])
            get.append(data[7])
            get.append(data[5])
            get.extend(data[0:3])

            [self.tool['entries'][i].delete(0,END) for i in range(5)]
            [self.tool['entries'][i].insert(0,get[i]) for i in range(5)]
            db.cache('cmd',True)
            db.cache('oid',data[-1])

            current_month = self.combo[2].index(self.combo[0].get())
            current_year = self.combo[3].index(int(self.combo[1].get()))

            self.zombo[0].current(current_month)
            self.zombo[1].current(current_year)

    def _qr(self):
        from qr import QR

        qr=QR(tab=self.tool['tab'],frame=self.tool['frames'][3])
        if self.type=='large':
            data=self.tree.item(self.tree.selection())['values']
        elif self.type=='small':    
            data=self.data
        qr.__qr__(data)

    def _chart(self):
        location=filedialog.askopenfile(initialdir='Desktop',title='Open File',defaultextension='.csv',filetype=[('Excel','*.csv')])
        from Plot import chart
        if location!=None:
            chart(location.name)

    def _xls(self):
        location=filedialog.asksaveasfile(initialdir='Desktop',title='Save As',defaultextension='.csv',filetype=[('Excel','*.csv')])
        try:
            with open(location.name,'a',newline='\n') as excelfile:
                header=['DOR','Month','Electricity','Waster','Waste','Rent','Total',
                'E-Present Meter','W-Present Meter',"E-Previous Meter",'W-Previous Meter']
                data = [list(i[0:-1]) for i in db.RS(int(self.combo[1].get()),'fetchall')]
                writer(excelfile,dialect='excel').writerow(header)
                for i in data:
                    writer(excelfile,dialect='excel').writerow(i)
        except AttributeError:
            pass