import datetime
import string
import os
import fnmatch
import csv
import xlrd
import re
from collections import OrderedDict
from time import gmtime, strftime
import pandas as pd

def ShowMe(x,n='x'):
    
    print '\n' + n + ':'
    
    if type(x) == list:
        for i,j in enumerate(x):
            print str(i) + ') ' + str(j)
            
    elif type(x) in [dict,type(OrderedDict())]:
        for i,j in enumerate(x):
            print str(i) + ') ' + str(j) + ' :' + str(x[j])
    elif type(x) == str:
        print x
            
    else:
        
        print 'What??'

def ReadCSV(p):

    X = []
    r = csv.reader(open(p, 'rU'))
    for row in r:
        X.append(row)
    return X


def Chose(x):
    while True:

        ShowMe(x)
        print "\n eg : 1,6,7"
        Choice = raw_input("    --Select from the choices above :").lower()
        print Choice
        
        if Choice in Everything:
            
            return x

        elif Choice in Quit:
            
            print 'Okay,Bye :)'
            return None

        else :

            try:

                IndexSelected = map(int,list(Choice.split(',')))
                print ShowMe(list( j for i,j in enumerate(x) if i in IndexSelected))
                OtherInput = raw_input('    --Are those the correct selections? :')
                print OtherInput

                if OtherInput in Negative:
                    print "Okay, give it another go"
                    
                elif OtherInput in Affermative + Everything:
                    print "Okay, great. Moving on"
                    return list( x for i,x in enumerate(x) if i in IndexSelected)
                    break

                else:
                    print "Unusual Entry!"

            except ValueError:

                print "There is an ValueError. This is probably because you entry in erroneous"
                print list(Choice.split(','))
    
    print 'Files Paths:'
    ShowMe(Choice)


def IfMakeDirs(IfMakeDirsPath):
    if not os.path.exists(IfMakeDirsPath):
        os.makedirs(IfMakeDirsPath)



def WriteCSV(WriteCSVOutData, WriteCSVFileName = 'PythonOutput',WriteCSVLocation = 'C:/Users/akhalifa/Desktop/Python - move forward/TXT/'):

    IfMakeDirs(WriteCSVLocation)
    
    WriteCSVOutputFile = WriteCSVLocation + WriteCSVFileName + '.csv'
    with open(WriteCSVOutputFile, 'wb') as WriteCSVOutputFileActive:
            writer = csv.writer(WriteCSVOutputFileActive,quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            try:
                    writer.writerows(WriteCSVOutData)
            finally:
                    WriteCSVOutputFileActive.close()


#       --  BEGIN --

#Responses
Affermative = ['yes','y','yup','yah']
Negative = ['no','n','nope','nah']
Quit = ['quit','q','exit','e']
Everything = ['','e','everything']

#Lux LOB Categories
Motor =  ['motor']
Medical = ['medical']
Other = ['miscellanous','accident','marineCargo','marine','hull','property','engineering']

#Lux Project Categories

Reserving = ['reserving']
Pricing = ['pricing']
Other = []

#Lux Catergories

Premium = ['premium','prem','premiums']
Outstanding = ['outstanding','os','clmos']
Paid = ['paid']
Claims = ['claims','cliam','clm']
TrialBalance = ['trial','balance','tb','trialbalance']
CAT = ['ct','cat']
OTHER = []

#Process Begins!!

PathInput = os.getcwd()

PythonCodeFolderPath = PathInput
PythonInputFolderPath=PythonCodeFolderPath.split("Python Code")[0] + "Python Input\\"
PythonOutputFolderPath=PythonCodeFolderPath.split("Python Code")[0] + "Python In But Not Out\\"

FilesPaths = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(PythonInputFolderPath)
    for f in files]

SelectedFilesPaths = FilesPaths#Chose(FilesPaths)
sfp = SelectedFilesPaths

ExcelFilesPaths = fnmatch.filter(sfp, '*.xls') + fnmatch.filter(sfp, '*.xlsx') + fnmatch.filter(sfp, '*.xlsm')
efp = ExcelFilesPaths

CSVFilesPaths = fnmatch.filter(sfp, '*.csv')
cfp = CSVFilesPaths

OtherFilesPaths = [x for x in sfp not in efp.extend(cfp)]
ofp = OtherFilesPaths

DataKey = []
for f in efp:
        print f

        wb = xlrd.open_workbook(f)
        Sheets = map(str,wb.sheet_names())

        for s in Sheets:
            
                print('Sheet: ' + str(s))
                
                ws = wb.sheet_by_name(s)

                Data = []
                DataWorked =[]
                DataExcluded = []
                for i in xrange(ws.nrows):
                        y = []
                        w = ws.row_values(i)
                        for x in w:
                                if type(x) == type(u''):
                                        x = x.encode('utf-8')
                                y.append(x)
                        Data.append(y)
                        
                counter = 0
        
                for i in Data:
                    if len(filter(None,i)) < (int(ws.ncols)*.5):
                        counter +=1
                        DataExcluded.append(i)
                    else:
                        DataWorked.append(i)

                print str(counter) + ' rows have insufficent data'

                counter += 1
                rowd = OrderedDict()
                fl = list(f.split('\\'))
                rowd['LA_SERIAL_NO'] =counter
                rowd["LA_PATH_INPUT"] = f
                
                rowd['LA_FILE_INPUT'] = fl[-1]
                rowd["LA_PATH_OUTPUT"] = PythonOutputFolderPath + rowd['LA_FILE_INPUT'] + '_' + str(s) + '.csv'
                
                for n in range(len(fl)):
                        rowd['LA_PATH_INPUT' +str(n+1)] = fl[n]
                fileNameListType = rowd['LA_FILE_INPUT'].rsplit(".",1)
                rowd['LA_FILE_NAME_INPUT'] = fileNameListType[0]
                if "." in fl[-1]:
                    rowd['LA_FILE_TYPE_INPUT'] = fileNameListType[1]

                rowd['LA_PATH_LIST_INPUT'] = map(lambda x:x.lower().replace('_',' '),f.split("\\"))
                rowd['LA_PATH_LIST_OUTPUT'] = map(lambda x:x.lower().replace('_',' '),(PythonOutputFolderPath + rowd['LA_FILE_INPUT'] + '_' + str(s) + '.csv').split("\\"))
                rowd["LA_CLIENT"] = rowd['LA_PATH_LIST_INPUT'][1]
                rowd["LA_PROJECT"] = rowd['LA_PATH_LIST_INPUT'][2]
                rowd["LA_PROJECT_STAGE_INPUT"] = rowd['LA_PATH_LIST_INPUT'][3]
                rowd['LA_EXCEL_SHEET_INPUT'] = s
                rowd['LA_DATETIME_STAMP'] = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                rowd['LA_DATETIME_STAMP_YQ'] =  str(int(strftime("%Y", gmtime()))*100 + int(strftime("%m", gmtime()))/3 + 1)
                rowd['LA_PATH_WORDS_INPUT'] = re.findall(r"[^\W\d_]+|\d+", (f+s).lower().replace('_',' '))
                
                try:
                    rowd['LA_HEADER_INPUT'] = DataWorked[0]
                except IndexError:
                    print f
                    print " This file has no DataWorked: /n " + str(f) + "_" + str(s)
                    pass

                
                #Lux Project
                for x in rowd['LA_PATH_LIST_INPUT']:
                    if x in Reserving:
                        rowd['LA_PROJECT_INPUT_1'] = 'Reseving'
                        break
                    elif x in Pricing:
                        rowd['LA_PROJECT_INPUT_1'] = 'Pricing'
                        break
                    else:
                        rowd['LA_PROJECT_INPUT_1'] = 'Other'

                
                #Lux LOB
                for x in rowd['LA_PATH_LIST_INPUT'] + list(rowd['LA_EXCEL_SHEET_INPUT']):

                    if x in Motor:
                        rowd['LA_LOB_1'] = 'Motor'
                        break
                    elif x in Medical:
                        rowd['LA_LOB_1'] = 'Medical'
                        break
                    else:
                        rowd['LA_LOB_1'] = 'Other'
                        break


                #Lux Categorization    
                for x in rowd['LA_PATH_LIST_INPUT'] + list(rowd['LA_EXCEL_SHEET_INPUT']):

                    if x in Premium:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'Premium'
                        break
                    elif x in Paid:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'Paid'
                        break
                    elif x in Outstanding:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'Outstanding'
                        break
                    elif x in TrialBalance:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'Trail Balace'
                        break
                    elif x in CAT:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'CAT'
                        break
                    else:
                        rowd['LA_LUX_CATEGORIZATION_1'] = 'Other'

                
                DataKey.append(rowd)
                
                WriteCSV(DataWorked,rowd['LA_FILE_INPUT'] + '_' + str(s) + '.csv',PythonOutputFolderPath)
                WriteCSV(DataExcluded,rowd['LA_FILE_INPUT'] + '_' + str(s) + '_Excluded.csv',PythonOutputFolderPath + "Excluded\\")

        kl = []

        for c in DataKey:
            for kk in c.keys():
                if kk not in kl:
                    kl.append(kk)

        k = set(kl)

        l =[]
        l.append(kl)


        for r in DataKey:
            row = []
            for h in l[0]:
                try:
                    row.append(str(r[h]))
                except KeyError:
                    row += "0"
            l.append(row)
        
        WriteCSV(l,'Key.csv',PythonOutputFolderPath + "Key\\")


