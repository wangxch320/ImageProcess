# -*- coding: utf-8 -*-
import os

print u"此程序会将监控文件夹下面的所有文件夹进行输出，最后将结果保存在与本程序同一目录下，输出文件名为result_check_filename.txt\n作者：青海师范大学生命与地理科学学院王兴春\n指导教师：赵霞\n"

morror_fold_name = raw_input(u"请输入监控文件夹名称")
result_check_filename = os.getcwd() + "\\result_check_filename.txt"
file_path = os.getcwd() + "\\%s" % morror_fold_name
f = open(result_check_filename,"w")
f.write("目录说明：本目录来自get_file_name.py程序生成，用来查看一个文件夹下面所有的文件夹，如果文件夹下面还包含文件夹，以文件夹名为标签，保存该文件夹下面的所有文件名\n\n作者：青海师范大学生命与地理科学学院王兴春\n指导教师：赵霞\n检测结果如下：")
num = 0
for name_list in os.walk(file_path):
    print u"文件夹",name_list[0].split("\\")[-1]
    f.write("文件夹%s\n" % (name_list[0].split("\\")[-1]))
    for file_name in name_list[2]:
        num = num + 1
        print u"文件",file_name
        f.write("%s\n" % file_name)
print u"共有%s个数据" % num
f.write("共有%s个数据" % num)
f.close()
