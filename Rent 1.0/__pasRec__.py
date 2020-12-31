#_______PASWORD_________#

#BuildInModule

from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

#Mymodule
import __scData__


def change_pasword():

	password_ui = Tk()

	#UiSetup
	password_ui.title('User Setup')
	password_ui.geometry('340x300+350+90')
	password_ui.resizable(0,0)


	#IconAndBackgroundSetup
	password_ui.iconbitmap('__img__\\Password_logo.ico')


	#TITLE
	Header = Label(password_ui,text=' User Setup',bg='#3b93e7',
		font=('new times roman',40,'bold')
		).place(x=0,y=0,relwidth=1)
	
	#InputBar'sSetUp
	input_bar = Entry(password_ui,width=20,borderwidth=5,show='λ')
	input_bar.place(x=150,y=100)
	display = Label(
		password_ui,text='Password',bg='#3b93e7',
		font=('new times roman','11','bold')
		).place(x=65,y=100)
	reinput_bar = Entry(password_ui,width=20,borderwidth=5,show='λ')
	reinput_bar.place(x=150,y=150)
	display = Label(
		password_ui,text='Renter-Password',bg='#3b93e7',
		font=('new times roman','11','bold')
		).place(x=10,y=150)

	#FunctionSetup
	def func_main(conform_pasword):
		__scData__.delete_pasword()
		store = __scData__.hex_converter(conform_pasword)
		__scData__.store_pasword(store)
		input_bar.delete(0,END)
		reinput_bar.delete(0,END)
		nextbutton = Button(
			password_ui,text=' Next',command=password_ui.destroy,width=10
			).place(x=260,y=273)


	def conform():

		new_pasword = input_bar.get()
		conform_pasword = reinput_bar.get()

		if new_pasword == conform_pasword:

			if len(new_pasword) >= 8 and len(conform_pasword) >= 8:
				
				a = Toplevel()
				a.geometry('250x120+500+250')
				this = Label(a,text=' Confrom Password ? ',font=('times new roman',14),
					).place(x=35,y=30)
				y= Button(a,text='Yes',width=8,command=lambda:[func_main(conform_pasword),a.destroy()]
					).place(x=35,y=80)
				n= Button(a,text='No',width=8,command=a.destroy).place(x=150,y=80)
			else:
				messagebox.showwarning(
					'Error',' Requirements not fulfilled ! Your Password must contain 8 characters.'
					)

		else:
			messagebox.showwarning('Error',' Your Password does not match !')

	conform = Button(
	password_ui,text=' Ok',
	command=conform
	).place(x=290,y=149)#func_main.functionexecution

	password_ui.mainloop()
#change_pasword()