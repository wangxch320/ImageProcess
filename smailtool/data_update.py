#!/usr/bin/env python
# -*-coding:utf-8 -*-
print "小量dbf表修改使用,2016年04月16日在青海师范大学 生命与地理科学学院编写"
from dbfpy import dbf

import os
path_now = os.getcwd()
print "当前路径",path_now
test_data_path = path_now + "//nong6.dbf"
data_dbf = path_now + "//polgon.dbf"


db_test = dbf.Dbf(test_data_path)
db = dbf.Dbf(data_dbf)
i = 0
for rec_test in db_test:
    for rec in db:
        if rec_test["ID"] == rec["ID"]:
            rec["GRIDCODE"] = 6
            print i,"成功修改"
            i = i + 1
            rec.store() ; del rec 
db.close() ; del i
db_test.close()
