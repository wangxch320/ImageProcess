# -*- coding: utf-8 -*-
import os
import datetime
import numpy as np

class daytomouth:
    def __init__(self):
        print "init"
    def oneyearonemouth(self, DayMirrorPath, StartYear, EndYear):
        print DayMirrorPath
        f = open(DayMirrorPath, "r")
        mouthpre = ""
        yearpre = ""
        tmpList = ["-"]*839
        accumulateDayNum = [0]*839
        for oneline in f.readlines():
            onelinesplit = (oneline.split("\n")[0]).split(",")
            year = onelinesplit[0][:4]
            mouth = onelinesplit[0][4:6]
            day = onelinesplit[0][6:8]
            if mouthpre == mouth:
                for i in xrange(839):
                    if onelinesplit[i+1] != "-":
                        if float(onelinesplit[i+1]) < 10000 and onelinesplit[i+1] != "-":
                            if tmpList[i] == "-":
                                tmpList[i] = 0
                            tmpList[i] = tmpList[i] + float(onelinesplit[i+1])/10
                            accumulateDayNum[i]+=1
            else:
                resultf = open("preresult.csv","a")
                print u"正在写%s年%s月,该月有效天数%s" % (year, mouth, accumulateDayNum[0])
                tmplistsave = []
                for x in xrange(len(tmpList)):
                    try:
                        tmplistsave.append(str(tmpList[x]))
                    except:
                        tmplistsave.append("-")
                resultf.write((str(yearpre) + str(mouthpre)) + ',' + ','.join(tmplistsave) + '\n')
                resultf.close()
                mouthpre = mouth
                yearpre = year
                tmpList = ["-"]*839
                accumulateDayNum = [0]*839
                for i in xrange(839):
                    if onelinesplit[i+1] != "-":
                        if float(onelinesplit[i+1]) < 10000 and onelinesplit[i+1] != "-":
                            if tmpList[i] == "-":
                                tmpList[i] = 0
                            tmpList[i] = tmpList[i] + float(onelinesplit[i+1])/10
                            accumulateDayNum[i]+=1

        tmplistsave = []
        for x in tmpList:
            try:
                tmplistsave.append(str(tmpList[x]))
            except:
                tmplistsave.append("-")
                            
        resultf = open("preresult.csv","a")
        resultf.write((str(yearpre) + str(mouthpre)) + ',' + ','.join(tmplistsave) + '\n')
        resultf.close()
        f.close()
        
if __name__ == "__main__":
    DayMirrorPath = u"C://Users//wangxch//Desktop//所需数据//PRE10dayresult.csv"
    StartYear = datetime.datetime(1951,1,1)
    EndYear = datetime.datetime(2016,12,31)
    pdaytomouth = daytomouth()
    pdaytomouth.oneyearonemouth(DayMirrorPath, StartYear, EndYear)
