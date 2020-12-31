#_______Rent_________#

from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from datetime import date

#MyModule
from __pasRec__ import change_pasword
from __updates__ import Widget
from __topLevel__ import Ui03
import __mainData__



#__PASSWORD_CHANGE__#
def Change_password():
	change_pasword()



#__MAIN_EXECUTION__#
def Rent():

	root = Tk()

	#__________UiSetup___________#

	#UiBasics
	root.title(' My Rent Record')
	root.iconbitmap('__img__\\logo.ico')
	root.geometry('1280x768+0+0')

	#ImageFiles:
	bg = ImageTk.PhotoImage(file='__img__\\background.jpg')
	ui2logo = ImageTk.PhotoImage(file='__img__\\Password_logo.ico')
	headerico = ImageTk.PhotoImage(file='__img__\\rent.png')
	conf00 = ImageTk.PhotoImage(file='__img__\\conform.png')
	n00 = ImageTk.PhotoImage(file='__img__\\next.ico')

	#BackGround
	background= Label(root,image=bg).pack()
	#BillsHeader
	Header = Label(
		root,image=headerico
				).place(x=600,y=320)
	
	#PaswordSetup
	pasword_switch_button = Button(root,image=ui2logo,bg='black',command=Change_password).place(x=0,y=0)


	#____________UpdateModule___________#                                 
	        								  	
	#Label                        				  
	label = Widget()
	                                
                                

	#____________________________SubHeader___________________________________#

	#Date
	label.Label(root,text='Date',fontSize=18,x=1000,y=29) 

	#Electricity
	label.Label(root,text='Electricity',fontSize=18,x=50,y=140)

	#Electricity__PreviousMeter
	label.Label(root,text='Previous Meter',x=50,y=250)

	#Electricity__PresentMeter
	label.Label(root,text='Present Meter',x=50,y=450)

	#Water
	label.Label(root,text='Water',fontSize=18,x=425,y=140)

	#WaterRate
	label.Label(root,text='Unit',x=425,y=200)

	#Water__PreviousMeter
	label.Label(root,text='Previous Meter',x=425,y=250)

	#Water__PresentMeter
	label.Label(root,text='Present Meter',x=425,y=450)

	#Waste
	label.Label(root,text='Waste',x=790,y=200)
	
	#Rent
	label.Label(root,text='Rent',x=1100,y=200)


	#______________________Input_Bar and Button:____________________#

	#ENTRY_BOX
	todays_date =  Entry(root,width=25,borderwidth=3)
	e_previous=Entry(root,width=30,borderwidth=3)
	e_now=Entry(root,width=30,borderwidth=3)
	w_previous = Entry(root,width=30,borderwidth=3)
	w_now=Entry(root,width=30,borderwidth=3)
	water=Entry(root,width=30,borderwidth=3)
	waste=Entry(root,width=30,borderwidth=3)
	rent=Entry(root,width=20,borderwidth=3)

	#PLACINGS
	todays_date.place(x=1070,y=30)
	e_previous.place(x=50,y=300)
	e_now.place(x=50,y=500)
	w_previous.place(x=425,y=300)
	w_now.place(x=425,y=500)
	water.place(x=510,y=147)
	waste.place(x=795,y=250)
	rent.place(x=1100,y=250)
	
	#INSERTS
	dd = date.today()
	todays_date.insert(0,dd.strftime("%B-%Y"))
	#water.insert(0,200)
	#waste.insert(0,175)
	#rent.insert(0,15000)


	#RADIOBUTTONSETUPS
	m=IntVar()
	m.set('12')
	Meter = [12]

	meter_11 = Radiobutton(
		root, text='11',bg='#ffffff',activebackground='pink',
		variable=m,value=11,command=lambda:[print(switch(11))]
		)
	meter_12 = Radiobutton(
		root, text='12',bg='#ffffff',activebackground='pink',
		variable=m,value=12,command=lambda: [print(switch(12))]
	)
	meter_11.place(x=495,y=205)
	meter_12.place(x=555,y=205)


	#_____________________INNERFUNTION_______________________#
		
	#DELETE
	def Delete():
		
		#INSERT_DELETE
		todays_date.delete(0,END)
		todays_date.insert(0,dd.strftime("%B-%Y"))
		water.delete(0,END)
		#water.insert(0,200)
		waste.delete(0,END)
		#waste.insert(0,175)
		rent.delete(0,END)
		#rent.insert(0,15000)
		
		#DELETE
		e_previous.delete(0,END)
		e_now.delete(0,END)
		w_previous.delete(0,END)
		w_now.delete(0,END)

		
	#SWITCH_RATE
	def switch(meter):

		del(Meter[0])

		if meter == 11:
			Meter.append(11)

		elif meter == 12:
			Meter.append(12)

		else: 
			Meter.append(12)


	#MAINFUNCTION
	def mainFunc():
		
		#Check_float
		def check01(date):

			try:
				e_pm = float(e_previous.get())
				e_nm = float(e_now.get())
				w_pm = float(w_previous.get())
				w_nm = float(w_now.get())
				Water = float(water.get())
				Waste=float(waste.get())
				Rent = float(rent.get())

			except ValueError:

				messagebox.showwarning('Error',' Invalid Value(s).')
			
			else:
				
				a = __mainData__.store_db00(
					Date=date,e_previous=e_pm,e_now=e_nm,w_previous=w_pm,w_now=w_nm,
					meter=Meter[0],Water=Water,Waste=Waste,Rent=Rent
				) 

				return a 

		#Check_entry_length
		def check00():

			condition = [
				len(str(todays_date.get()))==0,
				len(str(e_previous.get()))==0,
				len(str(e_now.get()))==0,
				len(str(w_previous.get()))==0,
				len(str(w_now.get()))==0,
				len(str(waste.get()))==0,
				len(str(rent.get()))==0
			]

			if any(condition):
				messagebox.showwarning('Error',' Incomplete input(s).')

			else:
				b = check01(todays_date.get())
				return b

		c = check00()

		if c == False:

			messagebox.showerror(' Error',' Record already exists! \n Create a unique record.')


	#_CONNECTION00_
	def Message():#CONFORMATION

		#GUI_Setup
		confrommessage = Toplevel()
		confrommessage.geometry('500x200+500+250')
		confrommessage.configure(bg='#3b93e7')
		confrommessage.resizable(0,0)
		label.Label(confrommessage,text='Are you sure you want to conform it ?',fontSize=18,x=50,y=50)
		

		#Button
		y = Button(confrommessage,text='Yes',width=10,
			command=lambda:[confrommessage.destroy(),mainFunc(),Delete()])
		y.place(x=65,y=150)

		n = Button(
			confrommessage,text='No',width=10,
			command=lambda : [confrommessage.destroy(),Delete()])
		n.place(x=350,y=150)


   

	finalize = Button(root,image=n00,command=Message).place(x=1240,y=600)

	file_logo = ImageTk.PhotoImage(file='__img__\\file_logo.png')
	show_result = Button(root,image=file_logo,command=lambda: [Ui03()]).place(x=1250,y=500)

	root.mainloop()#OkButton 


#Rent()