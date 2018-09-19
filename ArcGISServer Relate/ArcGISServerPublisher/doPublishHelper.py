# -*- coding: cp936 -*-

import sys,time
sys.path.append(r"D://Python27//ArcGIS10.1") # python文件路径
from publishHelper import PublishAll # 必须要有正确的许可，否则导入失败
from publishHelper import createMxdDocument # 必须要有正确的许可，否则导入失败
tiffFolder=time.strftime("%Y_%m_%d", time.localtime())
InData=r"F://code//python//Publisher//assist"
fname=r"dem30.tif"

createMxdDocument(r"F://code//python//Publisher//assist//model.mxd",InData, fname)
PublishAll(r"F://code//python//Publisher//assist", "http://localhost/ArcGIS/rest/services", "img")
