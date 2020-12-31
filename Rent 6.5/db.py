import sqlite3

class db:

    def RS(table_name,*args):
        
        conn = sqlite3.connect('tcl.db')
        rs=conn.cursor()

        table = [int(table_name)]
        
        rs.execute('''CREATE TABLE IF NOT EXISTS {}(
            DOR text,RecordforMonth text,Electricity INTEGER,
            Water INTEGER,Waste INTEGER,Rent INTEGER,
            Total INTEGER, em INTEGER, wm INTEGER, emp INTEGER, 
            wmp INTEGER
        )'''.format(table))
        
        try:
            if args[0]=='insert':
                data = args[1]
                rs.execute('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?,?,?)'.format(table),data)

            elif args[0]=='fetch':
                mid = [args[1]] #MonthId.
                rs.execute('SELECT *,oid FROM {} WHERE recordformonth=?'.format(table),mid)
                return rs.fetchall()

            elif args[0]=='fetchall':
                rs.execute('SELECT *,oid FROM {}'.format(table))
                return rs.fetchall()

            elif args[0]=='delete':
                oid = [args[1]]
                rs.execute('DELETE FROM {} WHERE oid=?'.format(table),oid)
            
            
        except sqlite3.OperationalError:
            pass
            
        
        conn.commit()
        conn.close()

    def cache(*args):
        conn = sqlite3.connect('Cache.db')
        ce=conn.cursor()

        def hexPascode(pascode):
            hexa =''
            for convert in range(len(pascode)):
                creating = hex(ord(pascode[convert]))
                hexa = hexa+creating
            return hexa
        
        fetch = 'SELECT {} FROM UI'
        update = '''UPDATE UI SET {} = ?'''
        
        wehave = ['user','password','bg','askpassword','fetch','alpha','meter','cmd','oid']
        weget = args[0]

        for i in range(len(wehave)):
            if weget == wehave[i]:
                ce.execute(update.format(wehave[i]),[args[1]])

            elif weget == wehave[4]:
                ce.execute(fetch.format(args[1]))
                for i in ce.fetchall(): 
                    for data in i:
                        return data
        conn.commit()
        conn.close()

    def PhotoLib(oid):
        conn = sqlite3.connect('Cache.db')
        plb = conn.cursor()
        plb.execute('SELECT oid,* FROM plb WHERE oid=(?)',[oid])
        for i in plb.fetchall():
            return i

        conn.commit()
        conn.close()