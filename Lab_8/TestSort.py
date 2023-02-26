import csv
import numpy as np
from Write import write_data
from WriteSR import writeSR
from tabulate import tabulate
#decrease
#import l

def sortT(val):
    with open('BankChurners.csv', 'r', ) as fbank:
        reader = csv.DictReader(fbank)
        sortedlist=np.sort(reader,order=val)
        #sortedlist = sorted(reader, reverse=True, key=lambda row: (row[val]))
        write_data(sortedlist)
        print(tabulate(sortedlist), end='\n')



    '''
    filedata=np.getfromcsv('BankChurners.csv',delimiter='')
    filedata[val]
    with open('BankChurners.csv', 'r', ) as fbank:
        reader = csv.DictReader(fbank)
        sl = np.array(reader)
        sl.sort(order=val)

        for row in reader:
            sl=np.array(row)
            #np.sort(sl,axis=0)
        write_data(np.sort(sl,axis=0))
        print(np.sort(sl,axis=0),end='\n')

        
        slist=np.genfromtxt(reader,delimiter=",")
        sortedlist=np.sort(slist,exis=0)
        #sortedlist=np.sort(order=val)
        '''