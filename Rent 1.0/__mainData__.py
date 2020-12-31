#________MAIN_DATA________#

import sqlite3 
from datetime import date

def Cal(e_previous,e_now,w_previous,w_now,meter):
	
	#calculation
	a = e_now - e_previous
	b = w_now - w_previous
	c = b/2
	d = a + c
	e = d*meter
	return e


def store_db00(Date,e_previous,e_now,w_previous,w_now,Water,Waste,Rent,meter):

	file = [str(Date)]
	Electricity = Cal(e_previous,e_now,w_previous,w_now,meter)
	Total = Electricity+Water+Waste+Rent
	Dd = date.today()
	Date = Dd.strftime('%a-%d-%b-%Y')
	amount = [Date,Electricity,Water,Waste,Rent,Total]

	conn = sqlite3.connect('#0x620x640x2e0x300x300x620x64.db')
	store = conn.cursor()
	#
	try:
		store.execute(""" 
			CREATE TABLE {}(
			Date text,
			Electricity INTEGER,
			Water INTEGER,
			Waste INTEGER,
			Rent INTEGER,
			Total INTEGER
			)
			
			""".format(file) 
			)

		store.execute(
			"""INSERT INTO {} VALUES (?,?,?,?,?,?)""".format(file),amount)

	except sqlite3.OperationalError:
		
		return False

	else:
		pass
	
	conn.commit()
	conn.close()
#
#
#

def display_db00(table_name):

	conn = sqlite3.connect('#0x620x640x2e0x300x300x620x64.db')
	out = conn.cursor()
	try:
		out.execute('SELECT * From {}'.format([str(table_name)]))
	except sqlite3.OperationalError:
		return False

	else:	
		a = out.fetchall()

		for j in a:
			get= j
		
		return get

	conn.commit()
	conn.close()

def delete_record(table_name):

	conn = sqlite3.connect('#0x620x640x2e0x300x300x620x64.db')
	
	delete = conn.cursor()
	delete.execute('DROP TABLE {}'.format(str([table_name])))

	conn.commit()
	conn.close()

	
