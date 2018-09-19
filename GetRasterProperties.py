# -*- coding:utf-8 -*-
if __name__=="__main__":
    import os

    path_now = os.getcwd()
    print "当前路径为%s" % path_now
    num = 0
    data_path = path_now + "\\mvresult2015"
    for data_ in os.walk(data_path):
        for data_name in data_[-1]:
            if data_name.endswith(".txt"):
                num = num + 1
                #print num,data_name
                f = open(path_now + "\\mvresult2015\\%s" % data_name,"r")
                for tmp in f.readlines():
                    temp = tmp.split("    ")
##                    if (((temp[-1].split("\n")))[0].split("="))[0] == "DATE_ACQUIRED ":
##                        #data
##                        print ((((temp[-1].split("\n")))[0].split("="))[1])[:11]
                    if (((temp[-1].split("\n")))[0].split("="))[0] == "CLOUD_COVER ":
                        #云
                        print (((temp[-1].split("\n")))[0].split("="))[1]
                f.close()
                

