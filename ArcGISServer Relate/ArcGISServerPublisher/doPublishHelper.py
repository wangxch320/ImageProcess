# -*- coding: cp936 -*-

import sys,time
sys.path.append(r"D://Python27//ArcGIS10.1") # python�ļ�·��
from publishHelper import PublishAll # ����Ҫ����ȷ����ɣ�������ʧ��
from publishHelper import createMxdDocument # ����Ҫ����ȷ����ɣ�������ʧ��
tiffFolder=time.strftime("%Y_%m_%d", time.localtime())
InData=r"F://code//python//Publisher//assist"
fname=r"dem30.tif"

createMxdDocument(r"F://code//python//Publisher//assist//model.mxd",InData, fname)
PublishAll(r"F://code//python//Publisher//assist", "http://localhost/ArcGIS/rest/services", "img")
