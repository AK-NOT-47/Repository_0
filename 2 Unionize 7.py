import datetime
import string
import os
import fnmatch
import csv
import xlrd
import re
from collections import OrderedDict
import pprint
from time import gmtime, strftime
import pandas as pd
from numpy import mean

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


def ShowMe2(x,n ='x'):
    
    for i in x:
        ShowMe(i)

	
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

                print "There is an ValueError. This is probably because your entry in erroneous"
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


def ReadCSVd(p):
    X = ReadCSV(p)

    Xd = OrderedDict()

    for h in X[0]:
        Xd[h] = []

    for e in X[1:]:

        c = 0

        for h in Xd.keys():
            
            Xd[h].append(e[c])

            c+=1
    
    return Xd


def Merge2Dicts(i, k):

    t3 = []
    for i2 in i:
        t3.append(len(i[i2]))

    t4 = []
    for k2 in k:
        t4.append(len(k[k2]))
    
    for k2 in k:
        if k2 in i.keys():
            i[k2] += k[k2]
        else:
            try:
                q = list('0'*max(t3))
                q.extend(k[k2])
                i[k2] = q
            except ValueError:
                i[k2] = k[k2]
    
    for i2 in i:
        if i2 not in k.keys():
            i[i2] += list('0'*max(t4))
    return i


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

#Lux File Catergories

Premium = ['premium','prem','premiums']
Outstanding = ['outstanding','os','clmos']
Paid = ['paid']
Claims = ['claims','cliam','clm']
TrialBalance = ['trial','balance','tb','trialbalance']
CAT = ['ct','cat']
Other = []

#Others
Empty = [""," ","0","-"]

#       -- BEGIN: The Second --

PathInput = os.getcwd()

PythonCodeFolderPath = PathInput
PythonInputFolderPath=PythonCodeFolderPath.split("Python Code")[0] + "Python In But Not Out\\"
PythonOutputFolderPath=PythonCodeFolderPath.split("Python Code")[0] + "Python In But Not Out\\Unioned\\"

FilesPaths = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(PythonInputFolderPath)
    for f in files]

SelectedFilesPaths = PythonInputFolderPath + 'Key\\Key.csv.csv'#Chose(FilesPaths) 

sfp = SelectedFilesPaths

ExcelFilesPaths = fnmatch.filter(sfp, '*.xls') + fnmatch.filter(sfp, '*.xlsx') + fnmatch.filter(sfp, '*.xlsm')

CSVFilesPaths = fnmatch.filter(sfp, '*.csv')

cfp = CSVFilesPaths
efp = ExcelFilesPaths

headersDict = OrderedDict()


FileXd = ReadCSVd(sfp)

ShowMe(FileXd.keys(),"Headers")

c = 0

X1d = OrderedDict()

for x0 in range(len(FileXd['LA_PATH_OUTPUT'])):
        
    print FileXd['LA_PATH_OUTPUT'][x0] + " , " + "\n" + FileXd['LA_HEADER_INPUT'][x0] + "\n" + "*" *50

    if FileXd['LA_HEADER_INPUT'][x0] in Empty:
        continue

    X1d[FileXd['LA_PATH_OUTPUT'][x0]] = FileXd['LA_HEADER_INPUT'][x0].split(",")


def Where(FileXd = FileXd,InputColumn ='LA_PATH_OUTPUT',Condition = "c",OutputColumn = 'LA_HEADER_INPUT'):

    wl = []
    
    for x0 in range(len(FileXd[InputColumn])):
        if FileXd[InputColumn][x0] == Condition:

            wl.append(FileXd[OutputColumn][x0])
    return wl

        #X1d[FileXd[InputColumn][x0]] = list(FileXd[OutputColumn][x0])





c2 = 0

llu = []
dlu = OrderedDict()

dlu['file1'] = []
dlu['file2'] = []
dlu['percentage'] = []

for x in X1d:
    
    if X1d[x] in Empty:
        continue

    c2+=1

    file1 = x#.rsplit("\\",1)[1]
    
    print '\n' + "*" * 50 + "\n" + file1

    print '\n' + str(len(X1d[x])) + '\n'

    c1 = 0
    for y in X1d:


        file2 = y#.rsplit("\\",1)[1]
        

        
        #llu.append([file1,file2,percentage])

        
        c = 0
        
        for x1 in X1d[x]:
            
            if x1 in X1d[y]:
                
                c += 1
                
        if float(c)/len(X1d[x]) > .75:

            if not x == y:

                percentage = float(c)/len(X1d[x])
                
                dlu['file1'].append(file1)
                dlu['file2'].append(file2)
                dlu['percentage'].append(percentage)
                
                print str(c1) + ")" + str(file2) + ") " + str(c) + " - " + str(float(c)/len(X1d[x]))# + " - " + str(percentage)
                c1 += 1
                
print '*' * 50 + '\n'

ShowMe(map(lambda x:x.rsplit("\\",1)[1],X1d.keys()))

x2 = dlu['percentage']

x5 = [str(x3) + "|" + str(x4) for x3,x4 in enumerate(x2) if x3>mean(x2)]
x6 = [(e,i) for i,e in enumerate(x2)]
x7 = sorted(x6,reverse=True)

ax = set()
ay = set()
axy = set()

r = [i1 for j1,i1 in x7]

print " \n union lists created: \n"


u = []

for i,j in x7:

    
    x8 = dlu['file1'][j]
    x9 = dlu['file2'][j]

    if not (x8  in axy or x9 in axy):

        u1 = [x8,x9]
        
        ax.add(x8)
        ax.add(x9)

        axy.add(x8)
        axy.add(x9)
        print '\n'
        print x8
        print str(j) + " " + x9

        for n in range(len(dlu['file1'])):
            
            if dlu['file1'][n] in [x8,x9] and n in r and n != j and (dlu['file2'][n] not in axy):

                y3 = dlu['file2'][n]

                ay.add(y3)

                axy.add(y3)

                u1.append(y3)
                print n,dlu['file2'][n]

        u.append(u1)

print '\n'*3
print "*" * 32
print '   "Union-Magic" is happening'
print "*" * 32

for u2 in u:

    u4 = OrderedDict()

    print '\n'*1
    
    for u3 in u2:

        fileX2 = ReadCSVd(u3 + '.csv')

        t2 = []
        for x in fileX2:
            
            t2.append(len(fileX2[x]))

        for x in fileX2:

            if len(fileX2[x]) < max(t2):

                print ' Not enough columns'
                print 'Max:  ' + str(max(t2))
                print x + ':  ' + str(len(fileX2[x]))

                x12 = ('0'*(max(t2)-len(fileX2[x])).split(","))
                fileX2[x].extend(x12)
                
            elif len(fileX2[x]) > max(t2):
                
                print 'what????'
                print 'Max:  ' + str(max(t2))
                print x + ':  ' + str(len(fileX2[x]))

            else:
                pass
                #print('perfect')
                                             

        x11 = ((str((u3.rsplit('\\',1)[1])) + ",")*max(t2)).split(",")
        
        del x11[-1]
        fileX2['LP_SOURCE'] = x11

        u4 = Merge2Dicts(u4,fileX2)
        print str((u3.rsplit('\\',1)[1]))


        del fileX2

    l = [list(u4.keys())]

    t = []
    for x in u4:

        t.append(len(u4[x]))

    if len(set(t))>1:
        print "Data irregularities:"
        print t
        
    for x10 in range(max(t)):
        row = []
        for x11 in u4.keys():

            try:
                row.append(u4[x11][x10])
            except KeyError and IndexError:
                row += "0"
        l.append(row)

    WriteCSV(l,u2[0].rsplit('\\',1)[1] + "_Unioned",PythonOutputFolderPath)

ShowMe2(u)
