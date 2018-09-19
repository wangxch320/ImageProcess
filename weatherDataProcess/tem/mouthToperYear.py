# -*- coding: utf- -*-
csv_data = "temresult.csv"
f = open(csv_data,"r")
preyear = "0000"
tmpList = ["-"]*839
accumulateMouthNum = [0]*839
for oneline in f.readlines():
    onelinesplit = (oneline.split("\n")[0]).split(",")
    year = onelinesplit[0][:4]
    mouth = onelinesplit[0][4:6]
    if year == preyear:
        for i in xrange(839):
            if onelinesplit[i+1] != "-":
                if float(onelinesplit[i+1]) < 10000 and onelinesplit[i+1] != "-":
                    if tmpList[i] == "-":
                        tmpList[i] = 0
                    tmpList[i] = tmpList[i] + float(onelinesplit[i+1])
                    accumulateMouthNum[i]+=1
    else:
        print preyear, year, mouth
        resultf = open("mouthToperYear.csv","a")
        print u"正在写%s年,该年有效月数%s" % (year, accumulateMouthNum[0])
        tmplistsave = []
        for x in xrange(len(tmpList)):
            try:
                tmplistsave.append(str(tmpList[x]/accumulateMouthNum[x]))
            except:
                tmplistsave.append("-")
        resultf = open("mouthToperYear.csv","a")
        resultf.write(str(preyear) + ',' + ','.join(tmplistsave) + '\n')
        resultf.close()
        preyear = year
        tmpList = ["-"]*839
        accumulateMouthNum = [0]*839
        for i in xrange(839):
            if onelinesplit[i+1] != "-":
                if float(onelinesplit[i+1]) < 10000 and onelinesplit[i+1] != "-":
                    if tmpList[i] == "-":
                        tmpList[i] = 0
                    tmpList[i] = tmpList[i] + float(onelinesplit[i+1])
                    accumulateMouthNum[i]+=1
tmplistsave = []
for x in xrange(len(tmpList)):
    try:
        tmplistsave.append(str(tmpList[x]/accumulateMouthNum[x]))
    except:
        tmplistsave.append("-")
resultf = open("mouthToperYear.csv","a")
resultf.write(str(preyear) + ',' + ','.join(tmplistsave) + '\n')
resultf.close()
                        
