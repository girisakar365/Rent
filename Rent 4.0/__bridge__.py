from tkinter import messagebox
from db import db

class Operation:

    def create_record(table,month,e_now,e_previous,w_now,w_previous,meter,water,waste,rent):
        
        def calculation():
            #calculation
            a = int(e_now) - int(e_previous)
            b = int(w_now) - int(w_previous)
            c = b/2
            d = a + c
            e = d*int(meter)
            return e
        
        def store():
            #store    
            from datetime import date
            time = date.today()
            splittime = time.strftime('%d/%b/%Y  %a')
            electricity = calculation()
            Total = electricity+int(water)+int(waste)+int(rent)
            raw = [splittime,month,electricity,water,waste,rent,Total,e_now,w_now]
            conn = db.insert_data(table,raw)
            return conn

        def check_gate():
            #Check
            if table == 'Month-Year':
                messagebox.showerror('Error: 411','Select a proper month and year.')
                return False
            else:
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
                
    def renew(pp,np,rnp):
        #check
        recieve = list(db.Password(pp,'get'))
        if recieve[0] == recieve[1]:
            condition = [
                len(str(pp)) == 0,
                len(str(pp)) < 8,
                len(str(pp)) > 32
            ] 
            if any(condition):
                messagebox.showerror('Security','Invalid password: Your password must atleast contain 8 to 32 chracters.')
            else:
                if np == rnp:
                    db.Password(rnp,'renew')
                    return True
                else:
                    messagebox.showerror('Security','Your password(s) did not match.')
                    return False
        else:
            messagebox.showerror('Security','Incorrect (Current) Password.')
            return False

    def log(pascode):
        password = pascode.get()
        if len(password) < 8 or len(password) > 32:
            messagebox.showerror('LOG-IN',' Ivalid password: Your password must contain 8 to 32 characters.')
        else:
            recived  = db.Password(password,'get')
            if recived[0] == recived[1]:
                return True
            else:
                messagebox.showerror('LOG-IN',' Incorrect password.')