from source import *
from db import db
 
class Setting:

    def __init__(self,*args,**kwargs):

        self.tool = {key:value for key,value in kwargs.items()}
        
        self.security = args[0]
        self.user = args[1]
        self.ui = args[2]
        self.back = args[3]
        self.reset=args[4]

        self.next = Dp.image_loader(db.PhotoLib(14)[1])

        #function:
        self.security['command']=self._security
        self.user['command']=self._user
        self.ui['command']=self._ui
        self.back['command']=self._back
        

    def hide(self):#hideandshowUpdate
        Dp(bg=setbg.currentbg())
        hd= Dp.text_label(self.tool['frame'],x=220,y=190)
        hd['bd'] = 550
        Dp.reset_key()

    def _security(self):#Security
        from genPascode import Password
        self.hide()
        Dp(fontSize=20,fontType='italic',bg=setbg.currentbg())
        Title = Dp.text_label(self.tool['frame'],text='  Security',x=390,y=225)#Title
        Dp(fontSize=14)
        subhead1 = Dp.text_label(self.tool['frame'],text='Current Password',x=380,y=285)#CurrentPassword
        subhead2 = Dp.text_label(self.tool['frame'],text='New Password',x=380,y=365)#NewPassword
        subhead3 = Dp.text_label(self.tool['frame'],text='Re-Enter Password',x=380,y=445)#Re-EntrePassword
        pascode=db.cache('fetch','password')
        
        Dp(width=30)
        self.tool['style'].configure('TEntry',foreground='#1d1f2a')
        current_password = Dp.entry(self.tool['frame'],x=380,y=330)#Entry1
        current_password.focus()
        ue1=Include.eye(self.tool['frame'],current_password,x=580,y=330)
        new_password = Dp.entry(self.tool['frame'],x=380,y=400)#Entry2
        update_eye=Include.eye(self.tool['frame'],new_password,x=580,y=400)
        re_password = Dp.entry(self.tool['frame'],x=380,y=485)#Entry3
        ue2=Include.eye(self.tool['frame'],re_password,x=580,y=485)
        def Gen():#Generates Random Password
            Dp(bg=setbg.currentbg()) 
            rand=Password.randomPassword()
            new_password.delete(0,END)
            new_password.insert(0,rand)
            update_eye[0]()
        bulb= Dp.image_loader(db.PhotoLib(31)[1])#Setting up image of generator
        generate = Dp.image_button(self.tool['frame'],image=bulb,x=610,y=395)
        generate['command']=Gen
        Tip(generate,'Generate Password')
        change = Dp.image_button(self.tool['frame'],self.next,x=600,y=550)

        def conformPassword():
            def keepPassword():
                termsandconditon=[len(new_password.get())<8,len(new_password.get())>32,len(re_password.get())<8,len(re_password.get())>32]
                if any(termsandconditon):
                    Msg('Your password must contain atleast 8 to 32 character. You may take help from password generator.')
                else: 
                    if new_password.get()==re_password.get():
                        db.cache('password',Password.hexPassword(re_password.get(),'encode'))
                        for i in (current_password,new_password,re_password):
                            i.delete(0,END)
                        current_password.focus()
                        Msg('Security successfully enabled.')
                    else:
                        Msg('Password Unmatched !')
            if db.cache('fetch','password')=='empty':
                keepPassword()

            else:
                if Password.hexPassword(db.cache('fetch','password'))!=current_password.get():
                    Msg('Incorrect Password !')
                else:
                    keepPassword()                         
        Include.onoff(self.tool['frame'],(current_password,new_password,re_password),(change,self.security,generate),
        (update_eye,ue1,ue2))
        change['command']=conformPassword

    def _user(self):#Set_user

        self.hide()
        Dp(fontSize=20,fontType='italic',bg=setbg.currentbg())
        subhead1 = Dp.text_label(self.tool['frame'],text='User Name',x=410,y=255)
        Dp(fontSize=14)
        subhead2 = Dp.text_label(self.tool['frame'],text=' What should I call you ?',x=370,y=325)
        
        Dp(width=30,bd=0)
        user = Entry(self.tool['frame'],bg=setbg.currentbg(),fg='#313035',font=('Bookman Old Style',16,'italic'),bd=0)
        user.place(x=390,y=365)
        user.focus()

        def user_id():
            if len(user.get()) < 2 or len(user.get())>14:
                Msg('The characters of your name must range from 2 to 14.')
            else:
                if db.cache('fetch','user') != 'Admin':
                    Msg('{} your name is set to {}'.format(db.cache('fetch','user'),user.get()))
                else:
                    Msg('{} your name is set to {}'.format('User',user.get()))
                db.cache('user',user.get())
                from random import choice
                User = db.cache('fetch','user')
                greetings = ['Hello','Hi','Welcome','Namaste']
                user.delete(0,END)
                greet = choice(greetings)
                for i in range(len(self.tool['DgC'])):
                    self.tool['DgC'][i][2].config(text='{}, {}'.format(greet,User))
        change = Dp.image_button(self.tool['frame'],self.next,x=565,y=405)

        change['command']=user_id


    def _ui(self):#Cutomize_Background
        self.hide()
        Dp(bg='#2c2f33')
        b = Dp.text_label(self.tool['frame'],x=295,y=320)
        b['width']=23
        b['height']=5
        Dp(fontType='italic',fontSize=20,bg=setbg.currentbg())
        subhead1=Dp.text_label(self.tool['frame'],text='Customize Backgound',x=300,y=225)
        Dp(fontSize=14)
        subhead2=Dp.text_label(self.tool['frame'],text='Select Colour:',x=320,y=302)
    
        Dp(bg='#4f5bd5',atvbg='#4f5bd5',bd=0,fontSize=10)
        one = Dp.text_button(self.tool['frame'],text='      ',x=315,y=340)
        Dp(bg='#fa7e1e',atvbg='#fa7e1e')
        two= Dp.text_button(self.tool['frame'],text='      ',x=385,y=340)
        Dp(bg='#ffdc73',atvbg='#ffdc73')
        three= Dp.text_button(self.tool['frame'],text='      ',x=455,y=340)
        Dp(bg='#f04747',atvbg='#f04747')
        four= Dp.text_button(self.tool['frame'],text='      ',x=525,y=340)
        Dp(bg='#2bc760',atvbg='#2bc760')
        five= Dp.text_button(self.tool['frame'],text='      ',x=315,y=390)
        Dp(bg='#d62976',atvbg='#d62976')
        six= Dp.text_button(self.tool['frame'],text='      ',x=385,y=390)
        Dp(bg='#fce9db',atvbg='#fce9db')
        seven= Dp.text_button(self.tool['frame'],text='      ',x=455,y=390)
        Dp(bg='#962fbf',atvbg='#962fbf')
        eight= Dp.text_button(self.tool['frame'],text='      ',x=525,y=390)

        Include.slider(self.tool['root'],self.tool['frame'])

        def updt_bg(conn=None):

            def reset():
                db.cache('bg',1)          #insertingDefaultDataIntoDataBase
                db.cache('user','Admin')
                db.cache('alpha',0.87)
                db.cache('askpassword','disabled')
                db.cache('password','empty')
                self.tool['root'].attributes('-alpha',0.87)#setTransparancyOfWindowTo-0.87
                from random import choice
                User = db.cache('fetch','user')
                greetings = ['Hello','Hi','Welcome','Namaste']
                greet = choice(greetings)#Greetings\randomModule\User
                for i in range(len(self.tool['DgC'])):#user.config
                    self.tool['DgC'][i][2].config(text='{}, {}'.format(greet,User))

            if conn == 'reset':
                reset()
            self.hide()
            bg = setbg.currentbg()#BackgroundSet
            self.tool['style'].configure('TCheckbutton',background=setbg.currentbg(),
            activebackground=setbg.currentbg())#CheckBoxConfig
            for i in self.tool['frames']:
                i.config(bg=bg)
            for i in self.tool['buttons']:
                i.config(bg=bg,activebackground=bg)
            for i in self.tool['lables']:
                i.config(bg=bg)
            for i in range(len(self.tool['DgC'])):
                try:
                    self.tool['DgC'][0][i].config(bg=bg)
                    self.tool['DgC'][1][i].config(bg=bg)
                    self.tool['DgC'][2][i].config(bg=bg)
                    self.tool['DgC'][3][i].config(bg=bg)
                except IndexError:
                    pass
            #HandlingSpecialCase
            Dp(bg=setbg.currentbg())
            hide1 = Dp.text_label(self.tool['frames'][1],'Please search your records.',x=30,y=345)
            hide1['width']=75
            hide1['height']=6          
            hidden=Dp.text_label(self.tool['frames'][0],text='  ',x=650,y=530)
            hidden['bd']=15
            self.tool['buttons'][1].config(state='normal')
            self.tool['_clear']()
            Dp(fontSize=48,bg=setbg.currentbg())#HideTheSettingBlockLable.config
            subtitle=Dp.text_label(self.tool['frame'],'Choose Options',x=257,y=277)
            Dp.reset_key()

        one['command']=lambda:[db.cache('bg',1),updt_bg()]
        two['command']=lambda:[db.cache('bg',2),updt_bg()]
        three['command']=lambda:[db.cache('bg',3),updt_bg()]
        four['command']=lambda:[db.cache('bg',4),updt_bg()]
        five['command']=lambda:[db.cache('bg',5),updt_bg()]
        six['command']=lambda:[db.cache('bg',6),updt_bg()]
        seven['command']=lambda:[db.cache('bg',7),updt_bg()]
        eight['command']=lambda:[db.cache('bg',8),updt_bg()]
        self.reset['command']=lambda:[
        Include.conform(lambda:[updt_bg('reset')],
        'RENT','Are your sure you wanna rest settings to default?')]
        Dp.reset_key()


    def _back(self):
        self.hide()
        Dp(fontSize=48,bg=setbg.currentbg())
        subtitle=Dp.text_label(self.tool['frame'],'Choose Options',x=257,y=277)
        Dp.reset_key()
        self.tool['tab'].select(0)