f = open("chinastation.csv", "r")
chinastation = ((f.readlines()[0]).split("\n"))[0].split(",")

qinghaistationindex = []

qinghaistationf = open("qinghaistation.csv", "r")
for oneqinghaistation in ((qinghaistationf.readlines()[0]).split("\n"))[0].split(","):
    qinghaistationindex.append(chinastation.index(oneqinghaistation)+1)
qinghaistationf.close()
f.close()


targetf = open("1.csv", "r")
resultf = open("tmplistsave.csv","a")
for oneline in targetf.readlines():
    onelinesplit = (oneline.split("\n")[0]).split(",")
    tmplistsave = []
    tmplistsave.append(onelinesplit[0])
    for i in xrange(len(qinghaistationindex)):
        tmplistsave.append(onelinesplit[qinghaistationindex[i]])
    resultf.write(','.join(tmplistsave) + '\n')
resultf.close()
targetf.close()
    
