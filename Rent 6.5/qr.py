"""
__File__: QR tab
Source of import:  main
Buttons import: qr
Lable import: Created_new
"""
import pyqrcode
from tkinter import BitmapImage

class QR:
    def __init__(self,**kwargs):

        self.tool = {key:value for key,value in kwargs.items()}


    def __qr__(self,data):

        from source import Dp,Msg
        
        try:
            results = """
            Rent Bill:

                Date: {}    
                
                Month: {}                      

                Electricity = {}
                
                Water = {}
                
                Waste = {}
                
                Rent = {}
                ------------------
                Total = {}
                """.format(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            
            self.tool['tab'].select(3)
            code = pyqrcode.create(results)
            photo = BitmapImage(data=code.xbm(scale=3))
            Dp(bg='#ffffff')
            Dp.image_label(self.tool['frame'],photo,x=340,y=215)
        except IndexError:
            Msg('Please select your record first.','!')
