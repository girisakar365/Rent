#_______LOGIN_________#

from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import __scData__  
from _main_ import Rent


def main_func():
	Rent()

def signin():

	root = Tk()

	#LoginWindowSetup 
	root.title(' Log In')
	root.iconbitmap('__img__\\login.ico')
	root.geometry('340x300+500+200')

	#BackgroundSetup
	next_but = ImageTk.PhotoImage(file='__img__\\next-button.png')
	background = ImageTk.PhotoImage(file='__img__\\avatar.png')
	set_backgroung = Label(root,image=background).place(x=35,y=50)

	#HeaderSetup
	Header = Label(
		root,text='User Log In ',bg='#3b93e7',fg='#ffffff',
		font=('times new roman',30,'bold')
		).place(x=0,y=0,relwidth=1)

	#InputBarSetup
	sub_header = Label(
		root,text='Password',bg='#3b93e7',fg='#ffffff',
		font=('times new roman',11,'bold')
		).place(x=30,y=150)
	input_bar = Entry(root,width=25,borderwidth=2,show='λ')
	input_bar.place(x=100,y=152)

	#Buttons_Setup

	def password():
		 
		pascode = __scData__.hex_converter(input_bar.get())
		orginal_pascode = __scData__.get_pasword()

		if pascode == orginal_pascode:
			input_bar.delete(0,END)
			messagebox.showinfo('Successful Login',' Welcome User')
			next_button = Button(
				root,image=next_but,
				command=lambda:[root.destroy(),main_func()]
				).place(x=300,y=262)

		else:
			input_bar.delete(0,END)
			messagebox.showerror('Error',' Not User')
		   
	conf00 = ImageTk.PhotoImage(file='__img__\\conform.png')
	login_button = Button(root,image=conf00,command=password).place(x=260,y=150)


	root.mainloop() 
signin()