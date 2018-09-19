# -*- coding: utf- -*-
csv_data = "temresult.csv"
tmpList = ["-"]*839
accumulateMouthNum = [0]*839
preyear = "0000"
for mouth0 in xrange(12):
    f = open(csv_data,"r")
    for oneline in f.readlines():
        onelinesplit = (oneline.split("\n")[0]).split(",")
        year = onelinesplit[0][:4]
        mouth = onelinesplit[0][4:6]
        if int(mouth) == mouth0 + 1:
            print year, mouth
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
    resultf = open("mouthToperYear1to1.csv","a")
    resultf.write(str(preyear) + ',' + ','.join(tmplistsave) + '\n')
    resultf.close()

    tmpList = ["-"]*839
    accumulateMouthNum = [0]*839
    
    f.close()
    
tmplistsave = []
for x in xrange(len(tmpList)):
    try:
        tmplistsave.append(str(tmpList[x]/accumulateMouthNum[x]))
    except:
        tmplistsave.append("-")
resultf = open("mouthToperYear1to1.csv","a")
resultf.write(str(preyear) + ',' + ','.join(tmplistsave) + '\n')
resultf.close()
            
            
    
        
        
