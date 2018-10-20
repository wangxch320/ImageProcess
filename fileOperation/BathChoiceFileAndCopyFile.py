# bach choice file to new folder
# The following example shows how to select the 22x22.png file
# from the C://Users//Thinkpad//Desktop//test folder and copy
# it to the Z:\wangxch\target folder.
# author:wangxch
# 2018/10/20

# -*- coding: utf-8 -*-
import os
import shutil

outPut = r"C://Users//Thinkpad//Desktop//test"
filePath = ur"Z:\wangxch\target"

for files in os.walk(filePath):
    for onefile in files[2]:
        if onefile.endswith("22x22.png"):
            pngfile = files[0] + "//" + onefile
            pngFileName =  onefile.split("22x22.png")[0] + ".png"
            pngOutPath = outPut + "//" + pngFileName
            print pngfile, pngOutPath
            shutil.copyfile(pngfile,pngOutPath)

print "finished"
