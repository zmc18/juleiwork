from numpy import *
from itertools import groupby
import sys
import numpy
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = []
    
        
        for each in curLine:
            
            try:
                fltLine.append(float(each))
            except Exception,e:
                fltLine.append(float("nan"))
                print "wrong:%s"%curLine[-1]
           
        dataMat.append(fltLine)
    return dataMat

def writekmeans(dataname):
    
    fw = open(r'D:\zmc\machine-learning\juleiwork\juleizhengli.txt', 'w') 
    for i in range(len(dataname)):
        for j in range(6):
            fw.write('%f\t' %  dataname[i,j])
        fw.write('%f\n' %  dataname[i,-1])
    fw.close()



def replaceNanWithhourmean(dataset):
    dataMat = mat(dataset)
    for j in range(1,8):
        dataMathour = dataMat[dataMat[:,0].flatten().A[0]==j]
        num = shape(dataMathour)[1]
        for i in range(num):
            meanVal = mean(dataMathour[nonzero(~isnan(dataMathour[:,i].A))[0],i]) 
            dataMat[nonzero(isnan(dataMat[:,i].A))[0],i] = meanVal  #set NaN values to mean
            
    return dataMat   
print 'lalla'    

sys.path.append("D:\zmc\machine-learning\juleiwork")
print 'ola'
datayunsuan = loadDataSet('D:\zmc\machine-learning\juleiwork\wenyuan2.txt')
mynewdata = replaceNanWithhourmean(datayunsuan)
print 'ok'
print mynewdata[1]
print mynewdata[1,0]
writekmeans(mynewdata)