# -*- coding: utf-8 -*-
import os
import tarfile
import traceback

class Statistics():
    def __init__(self, monitorPath):
        self.monitorPath = monitorPath
        print "statistics start..."
        print "statistics target is %s" % self.monitorPath
    def LandsatExtract(self, tar_path, target_path):
         try:
             tar = tarfile.open(tar_path, "r:gz")
             file_names = tar.getnames()
             for file_name in file_names:
                 if file_name.endswith("_MTL.txt"):
                     if os.path.exists(target_path+file_name) == True:
                         os.remove(target_path+file_name)
                     tar.extract(file_name, target_path)
             tar.close()
             return "success"
         except Exception, e:
             return traceback.format_exc()
            
    def StatisticsLandsat8(self):
        if os.path.exists("StatisticResult.csv") == False:
            f=open("StatisticResult.csv", "a+")
            f.close()
        f = open("StatisticResult.csv", "r+")
        

        NumFile = 0
        successRecodeFile = 0
        for filenames in os.walk(self.monitorPath):
            fileFolderIn = filenames[0]
            print fileFolderIn
            for filename in filenames[2]:
                if filename.endswith(".tar.gz"):
                    NumFile+=1
                    inforecode = ""
                    inforecodeFied = ""
                    targzfile = fileFolderIn + "\\" + filename
                    print targzfile
                    target_path = "%s\\" %fileFolderIn
                    extractInfo = self.LandsatExtract(targzfile, target_path)
                    if extractInfo == "success":
                        _MTLtxtFile = target_path+(filename.split("."))[0] + "_MTL.txt"
                        try:
                            _MTLtxt = open(_MTLtxtFile,"r")
                            lines = _MTLtxt.readlines()
                            for oneline in lines[:-1]:
                                tmp = (oneline.split("\n"))[0]
                                inforecode = inforecode + "," + (tmp.split(" = "))[1]
                                inforecodeFied = inforecodeFied + "," + (tmp.split(" = "))[0].replace("    ","").replace("  ","")
                            _MTLtxt.close()
                            os.remove(_MTLtxtFile)
                            errorinfo = ""
                        except Exception, e:
                            print traceback.format_exc()
                            errorinfo = traceback.format_exc()
                    else:
                        print u"%s解压失败" % targzfile
                        print extractInfo
                        
                    if inforecode == "" and errorinfo == "":
                        f.write("%s,file extract fail%s\n" % (targzfile, extractInfo))
                    elif errorinfo != "":
                        f.write("%s,file _MTL.txt Open fail%s\n" % (targzfile, extractInfo))
                    else:
                        f.write("%s,%s,%s\n" % (targzfile,os.path.getsize(targzfile),inforecode))

        f.write(",tar.gz filesize,%s\n" % inforecodeFied)
        
        print "Total File Numbers %s" % NumFile
        f.write("Total File Numbers,%s,successRecodeFile Numbers,%s\n" % (NumFile,successRecodeFile))
        f.write("monitorPathis,%s\n" % self.monitorPath)
        
        f.close()

if __name__ == "__main__":
    print "please wait a moment, program starting"
    
    monitorPath = "C:\\Users\\Administrator\\Personal\\data\\dataDownloads"
    statistics = Statistics(monitorPath)
    statistics.StatisticsLandsat8()
