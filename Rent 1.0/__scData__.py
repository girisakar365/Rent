#__PascodeData__#
import sqlite3

def hex_converter(pasword):
	pascode = pasword[::-1]
	convert=''
	for i in  range(len(pascode)):
		hexcode = hex(ord(pasword[i]))
		convert = hexcode + convert

	return convert

def delete_pasword():

	conn = sqlite3.connect('#0x1620x640x2e0x310x300x620x64.db')
	#creat a cursor
	store = conn.cursor()
	#execute store
	store.execute("DELETE FROM pasword ")
	conn.commit()
	conn.close()


def store_pasword(pascode):

	pas = [pascode]
	conn = sqlite3.connect('#0x1620x640x2e0x310x300x620x64.db')
	#creat a cursor
	store = conn.cursor()
	#execute store
	store.execute("INSERT INTO pasword VALUES (?) ",pas)
	conn.commit()
	conn.close()


def get_pasword():

	conn = sqlite3.connect('#0x1620x640x2e0x310x300x620x64.db')
	out = conn.cursor()
	out.execute('SELECT * From pasword')
	
	a = out.fetchone()

	for j in a:
		pasword = j
	return pasword
	conn.commit()
	conn.close()