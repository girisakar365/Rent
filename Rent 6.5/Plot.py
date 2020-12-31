from matplotlib import pyplot as p
import csv
from source import Msg

def chart(location):
    Month=[]
    Total=[]

    with open(location,'r') as csv_file:

        csvfile = csv.DictReader(csv_file)
        
        try:
            for i in csvfile:
                Month.append(i['Month'])
                Total.append(float(i['Total']))
                    
        except KeyError:
            Msg('Your have selected a wrong file.','!')

        else:
            p.figure('Record Analysis')
            p.title('Analysis in Bar Chart')
            p.bar(Month,Total)
            p.show()