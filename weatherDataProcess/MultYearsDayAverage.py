# -*- coding: cp936 -*-
import os
f = open("PRE10dayresult1951to1981.csv", "r")
preYear = 0
stationNum = 839

srartyear = 1951
endyear = 1981
dayList = [["-" for i in xrange(366)] for j in xrange(stationNum)]
for oneline in f.readlines():
    onelineSplit = oneline.split("\n")[0]
    onelineSplitByDH = onelineSplit.split(",")

    year = int(onelineSplitByDH[0][:4])
    mouth = int(onelineSplitByDH[0][4:6])
    day = int(onelineSplitByDH[0][6:8])
    days = int(onelineSplitByDH[0][8:11])

##    print year, mouth, day, days
    if (year % 4 == 0) & (year % 100 != 0):
        for stationindex in xrange(len(onelineSplitByDH) - 1):
            if onelineSplitByDH[stationindex + 1] != "-":
                if(float(onelineSplitByDH[stationindex + 1]) < 10000):
                    if dayList[stationindex][days-1] == "-":
                        dayList[stationindex][days-1] = 0
                    dayList[stationindex][days-1]+=float(onelineSplitByDH[stationindex + 1])/10
    else:
        for stationindex in xrange(len(onelineSplitByDH) - 1):
            if onelineSplitByDH[stationindex + 1] != "-":
                if(float(onelineSplitByDH[stationindex + 1]) < 10000):
                    if days > 28:
                        if dayList[stationindex][days] == "-":
                            dayList[stationindex][days] = 0
                        dayList[stationindex][days]+=float(onelineSplitByDH[stationindex + 1])/10
                    else:
                        if dayList[stationindex][days-1] == "-":
                            dayList[stationindex][days-1] = 0
                        dayList[stationindex][days-1]+=float(onelineSplitByDH[stationindex + 1])/10
f.close()

resultList = ["-" for i in xrange(stationNum)]
for stationindex in xrange(stationNum):
    resultList[stationindex] = sum(filter(lambda x: x != "-", dayList[stationindex]))/(endyear - srartyear + 1)
print resultList[1]
f =open("result.csv","a")
f.write(','.join(map(str,resultList)) + "\n")
f.close()
