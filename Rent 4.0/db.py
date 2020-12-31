import sqlite3
from tkinter import messagebox

class db:

    #PASSIVE_DATABASE
    def Password(pascode='',condition=''):

        def convert(): 
            #convert
            hex_pascode = ''
            for i in range(len(pascode)):
                con = hex(ord(pascode[i]))
                hex_pascode = con + hex_pascode
            return hex_pascode

        def pascode_renew():
            
            hex_pascode = convert()
            #insert
            conn = sqlite3.connect('#0x640x620x300x310x2e0x640x62.db')
            create = conn.cursor()
            create.execute('DELETE FROM password')
            create.execute('INSERT INTO password VALUES (?)',[hex_pascode])
            conn.commit()
            conn.close()
            return True
        
        def get_pascode():
            b = convert()
            conn = sqlite3.connect('#0x640x620x300x310x2e0x640x62.db')
            get = conn.cursor()
            get.execute('SELECT * FROM password')
            got = get.fetchone()
            for i in got:
                return i,b
        
        if condition=='renew':
            return pascode_renew()
        elif condition=='get':
            return list(get_pascode())
        else:
            pass

    #ACTIVE_DATABASE
    def insert_data(date,data):
        
        conn = sqlite3.connect('#0x640x620x300x300x2e0x640x62.db')
        create = conn.cursor()

        try:
            create.execute(
                '''
                CREATE TABLE {}(

                DateofRecord text,
                RecordforMonth text,
                Electricity INTEGER,
                Water INTEGER,
                Waste INTEGER,
                Rent INTEGER,
                Total INTEGER,
                em1 INTEGER,
                wm1 INTEGER
                ) 
                '''.format([date])
            )

            create.execute('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'.format([date]),data)
        except sqlite3.OperationalError:
            messagebox.showerror('Error: 302','{} record already exists.'.format(date))
            return False
        else:
            conn.commit()
            conn.close()
            return True

    def delete_table(table_name):

        conn = sqlite3.connect('#0x640x620x300x300x2e0x640x62.db')
        remove = conn.cursor()
        try:
            remove.execute('DROP TABLE {}'.format([table_name]))
        except sqlite3.OperationalError:
            messagebox.showerror('Error: 303','Record not found!')
            return False
        else:
            conn.commit()
            conn.close()

    def dispaly_table(table_name):

        conn = sqlite3.connect('#0x640x620x300x300x2e0x640x62.db')
        display = conn.cursor()

        try:
            display.execute('SELECT * FROM {}'.format([table_name]))

            data = display.fetchall()

            for i in data:
                data = list(i)
            return data
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
            messagebox.showerror('Error: 304','{} does not contain any record!'.format(table_name))
            return False
    
    def cache(data,condition):

        def insert():
            conn = sqlite3.connect('Cache.db')
            bring = conn.cursor()
            bring.execute('DELETE FROM bg WHERE bg_no;')
            bring.execute('INSERT INTO bg VALUES (?)',[data])
            conn.commit()
            conn.close()
        
        def get():
            conn = sqlite3.connect('Cache.db')
            bring = conn.cursor()
            bring.execute('SELECT * FROM bg')
            a = bring.fetchone()
            return a
            conn.commit()
            conn.close()
        if condition == 'insert':
            insert()
        elif condition == 'get':
            for i in  get():
                return i

    def cache2(data,condition):
        
        def insert():
            if len(data)>15 or len(data)<3:
                messagebox.showerror('User',' Your name must NOT contain more than 15 characters and less than 3 characters.')
                return False
            else:
                conn = sqlite3.connect('#0x640x620x300x310x2e0x640x62.db')
                bring = conn.cursor()
                bring.execute('DELETE FROM user')
                bring.execute('INSERT INTO user VALUES (?)',[data])
                conn.commit()
                conn.close()
        
        def get():
            conn = sqlite3.connect('#0x640x620x300x310x2e0x640x62.db')
            bring = conn.cursor()
            bring.execute('SELECT * FROM user')
            a = bring.fetchone()
            return a
            conn.commit()
            conn.close()
        if condition == 'insert':
            insert()
        elif condition == 'get':
            try:
                for i in  get():
                    return i
            except TypeError:
                return False