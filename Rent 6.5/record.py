"""
__File__: record tab
Source of import:  main
Buttons import: Clear, Confrom Record,edit,delete,qr
Lable import: no_record, dor
combo import: src, ssr,
"""

from source import *
from db import db
from Tree import Tree

class Record:
    def __init__(self,*args,**kwargs):

        self.tool={key:value for key,value in kwargs.items()}

        self.clear = args[0]
        self.record = args[1]
        self.today = strftime('%d/%m/%Y')
        
        self.combo = self.tool['combo']

        self.clear['command']=self._clear
        self.record['command']=self._record


    def _clear(self):
        self.tool['entries'][0].delete(0,END)
        self.tool['entries'][1].delete(0,END)
        self.tool['entries'][2].delete(0,END)
        self.tool['entries'][3].delete(0,END)
        results=None
        for i in db.RS(self.combo[0][1].get(),'fetch',strftime('%B')):
            results=i
        #Handeling Previous Meter inserting problem
        try:
            try:
                self.tool['entries'][0].insert(0,results[7])
                self.tool['entries'][2].insert(0,results[8])
            except TypeError:
                pass
        except IndexError:
            pass
        self.tool['entries'][1].focus()
        db.cache('cmd',False)
        db.cache('oid',None)

    def _record(self):
        
        Conn = Gate(cmd=db.cache('fetch','cmd'),entries=self.tool['entries'],combo=(self.combo[0][0],self.combo[0][1]))

        if Conn.check() == True:
            
            #DisplayStuff
            self.tool['tab'].select(1)  
            current_month = self.combo[0][2].index(self.combo[0][0].get())
            current_year = self.combo[0][3].index(int(self.combo[0][1].get()))
            self.combo[1][0].current(current_month)
            self.combo[1][1].current(current_year)
        
            self.tool['engine']()

            self.tool['entries'][1].delete(0,END)
            self.tool['entries'][3].delete(0,END)
            self.tool['entries'][1].focus()
            self._clear()
            
class Gate:#ErrorHandels

    def __init__(self,cmd=0,**kwargs):#initializating-widget
        self.gate={keys:values for keys,values in kwargs.items()}
        self.cmd=cmd

    def check(self):#mainCheckGateOfRecord-Section
        intake=[i.get() for i in self.gate['entries'] if len(i.get())!=0]
        if len(intake)<7:
            Msg('Opps! Your input(s) is missing.','!')
        elif self.gate['combo'][0].get()=='Month' or self.gate['combo'][1].get()=='Year':
            Msg('Please select an appoprite month or year.','!')
        else:
            try:
                checkalpha=[int(i) for i in intake]
            except ValueError:
                Msg('Your input(s) must always be a number NOT an alphabet','!')
            else:
                if db.cache('fetch','meter')==0:
                    Msg('Opps! You haven\'t selected unit.','!')
                else:
                    self.store()
                    return True

    def store(self):#mainStoreFunction
        if self.cmd!=0:
            db.RS(self.gate['combo'][1].get(),'delete',db.cache('fetch','oid'))

        eleclist=[int(i.get()) for i in self.gate['entries'][0:4]]
        water = int(self.gate['entries'][4].get())
        waste = int(self.gate['entries'][5].get())
        rent = int(self.gate['entries'][6].get()) 
        electricity = ((eleclist[1]-eleclist[0])+((eleclist[3]-eleclist[2])/2))*db.cache('fetch','meter')
        Total = electricity+water+waste+rent
        raw = [strftime('%d/%m/%Y'),self.gate['combo'][0].get(),
        electricity,water,waste,rent,Total,
        eleclist[1],eleclist[3],eleclist[0],eleclist[2]]
        db.RS(self.gate['combo'][1].get(),'insert',raw)
