"""
File: Main
This file is the main distribution system of all the widget made in the FRONT-END file.
Takes all the file and distributes it (required widget) to different tabs.
"""
class BackEnd:

    def __init__(self,*args,**kwargs):
        self.btw_dict = {
            'clear_1': args[0],'conform': args[1],'search': args[2],
            'edit': args[3],'delete': args[4],'qr': args[5],
            'clear_2':args[6],'security':args[7],'user_id':args[8],
            'cbg':args[9],'back':args[10],'reset':args[11],'remove':args[12],
            'trash_qr':args[13],'xls':args[14],'chart':args[15]
        }#Button Dictionary
        
        self.access = {keys:values for keys,values in kwargs.items()}

        self._engine=None
        self._clear=None

        self._Search()
        self._Record()
        self._Setting()

    def _Record(self):
        from record import Record#Record-Section

        record_section=Record(
            self.btw_dict['clear_1'],
            self.btw_dict['conform'],
            tab=self.access['tab'],
            frames=self.access['frame'][0],
            frame=self.access['frame'][1],
            entries=self.access['entries'],
            edit=self.btw_dict['edit'],
            delete=self.btw_dict['delete'],
            qr=self.btw_dict['qr'],
            xls=self.btw_dict['xls'],
            lable=(self.access['lables'][0],self.access['lables'][8]),
            combo=(self.access['combo']),#record_sections\widgetDistrubution\
            engine=self._engine
)        
        self._clear=record_section._clear
        
    def _Search(self):
        from search import Search

        search_section=Search(
            self.btw_dict['clear_2'],
            self.btw_dict['search'],
            self.btw_dict['delete'],
            self.btw_dict['edit'],
            self.btw_dict['qr'],
            self.btw_dict['xls'],
            self.btw_dict['chart'],
            lables=(self.access['lables'][0],self.access['lables'][8]),
            tab=self.access['tab'],
            combo=self.access['combo'][1],
            zombo=self.access['combo'][0],
            frame=self.access['frame'][1],
            entries=self.access['entries'],
            frames=self.access['frame'],
        )#search_sections\widgetDistrubution\

        self._engine=search_section._search

    def _Setting(self):
        from setting import Setting

        setting_section=Setting(  #setting_sections\widgetDistrubution\
            self.btw_dict['security'],self.btw_dict['user_id'],
            self.btw_dict['cbg'],self.btw_dict['back'],self.btw_dict['reset'],
            frame=(self.access['frame'][2]),
            frames=(self.access['frame']),
            DgC=self.access['DgC'],
            root=self.access['root'],
            tab=self.access['tab'],
            reset=self.btw_dict['reset'],
            style=self.access['style'],
            lables = self.access['lables'],
            buttons=(
                self.btw_dict['clear_1'],self.btw_dict['conform'],self.btw_dict['search'],
                self.btw_dict['delete'],self.btw_dict['qr'],self.btw_dict['edit'],
                self.btw_dict['clear_2'],self.btw_dict['reset'],self.btw_dict['trash_qr'],self.btw_dict['xls'],
                self.btw_dict['chart']),
            entries=self.access['entries'],
            _clear=self._clear
        )
