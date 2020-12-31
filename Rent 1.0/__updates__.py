from tkinter import *

class Widget:

	def Label(self,win,text='',bg='#3b93e7',fontType='bold',fontSize=14,x=0,y=0):
		self = Label(
			win,text=text,bg=bg,font=('times new roman',fontSize,fontType)

			).place(x=x,y=y)


		
	def Button(self,win,text,cmd,width=0,x=0,y=0):

		self = Button(win,text=text,width=width,command=cmd)
		self.place(x=x,y=y)
		self.bind('<Enter>',button)
