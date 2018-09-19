# -*- coding: utf-8 -*-
import arcpy, os,time

__name__ = 'publishHelper'

# 将指定目录下所有的.mxd文档发布为地图服务
# folder：包含mxd文档的文件夹路径
# serviceDir：服务目录URL，例如http://localhost/arcgis/rest/services
# serviceFolder：服务所在文件夹，如果为空，则表示根目录
def PublishAll(folder,serviceDir,serviceFolder):
    print "检查文件夹路径……"
    if os.path.isdir(folder) == False:
        print "输入的文件夹路径无效！"
        return
    print "遍历文件夹……"
    files = os.listdir(folder)
    for f in files:
        if f.endswith(".mxd"):
            mxdPath = os.path.join(folder, f)
            print "publishing: " + f
            PublishMxd(f,mxdPath, serviceDir, serviceFolder)
        else:
            continue
#将mxd文档发布为服务：1.将mxd转为msd；2.分析msd；3.发布msd
def PublishMxd(mxdName,mxdPath, serviceDir, serviceFolder):
    #检查mxd文件是否存在
    print "检查文件路径……"
    if os.path.exists(mxdPath) == False:
        print "指定路径的mxd文档不存在！"
        return
    
    # 打开mxd文档
    try:
        print "正在打开mxd文档……"
        mxd = arcpy.mapping.MapDocument(mxdPath)
    except Exception, e:
        print "open mxd error: ", e
        return
    else:
        print "mxd文档打开成功……"

    # 获取默认的数据框
 

    # 构造sddraft文档名称
    con = 'C://Users//wangxch//AppData//Roaming//ESRI//Desktop10.1//ArcCatalog//arcgis on localhost_6080 (admin).ags'
    sddraft = mxdPath.replace(".mxd", ".sddraft")
    service=mxdName.replace(".mxd", "")
    #sd=mxdPath.replace(".mxd", ".sd")
    #sd = con + "//" + os.path.split(os.path.splitext(mxdPath)[0])[1] + ".sd"
    #sd = "C://Users//wangxch//AppData//Roaming//ESRI//Desktop10.1//ArcCatalog//" + os.path.split(os.path.splitext(mxdPath)[0])[1] + ".sd"
    #sd = "C://Users//wangxch//temp//" + os.path.split(os.path.splitext(mxdPath)[0])[1] + ".sd"

##    if os.path.exists('C://Users//wangxch//temp') == False:
##        os.mkdir('C://Users//wangxch//temp')
    sd = "F://" + os.path.split(os.path.splitext(mxdPath)[0])[1] + ".sd"
    copy_data_to_server=True
    #正在将mxd文档转换为sddraft文档……"
    # Create service definition draft
    arcpy.mapping.CreateMapSDDraft(mxd, sddraft, service,'ARCGIS_SERVER',con,copy_data_to_server, serviceFolder)
    # Analyze the service definition draft
    analysis = arcpy.mapping.AnalyzeForSD(sddraft)
    
    # Print errors, warnings, and messages returned from the analysis
    print "The following information was returned during analysis of the MXD:"
    for key in ('messages', 'warnings', 'errors'):
      print '----' + key.upper() + '---'
      vars = analysis[key]
      for ((message, code), layerlist) in vars.iteritems():
        print '    ', message, ' (CODE %i)' % code
        print '       applies to:',
        for layer in layerlist:
            print layer.name,
        print

    print "Publishing"
    print sddraft, sd
    # Stage and upload the service if the sddraft analysis did not contain errors
    if analysis['errors'] == {}:
        # Execute StageService. This creates the service definition.
        arcpy.StageService_server(sddraft, sd)
        print "sddraft, sd"
        #Execute UploadServiceDefinition. This uploads the service definition and publishes the service.
        arcpy.UploadServiceDefinition_server(sd, con)
        print "Service successfully published"
    else: 
        print "Service could not be published because errors were found during analysis."
    print arcpy.GetMessages()
    os.remove(sd)

# demoMXDPath：包含mxd文档名称
# folder：包含新建的mxd文档以及tiff文件的文件夹路径
def createMxdDocument(demoMXDPath,InData, fname):
     if os.path.exists(demoMXDPath) == False:
        print "mxd document it's not exist!"
        print "demoMXDPath:%s" % demoMXDPath
     else:
        try:
            i = 0
            print "opening mxd document……"
            mxd = arcpy.mapping.MapDocument(demoMXDPath)
            print "repair layer source"

            df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
            print arcpy.mapping.ListLayers(mxd, "", df)[i].name
            lyr = arcpy.mapping.ListLayers(mxd, "", df)[i]
            print InData,"RASTER_WORKSPACE",fname
            lyr.replaceDataSource(InData,"RASTER_WORKSPACE",fname)

            lyr.name=fname.replace(".tiff", "")

            mxdName=time.strftime("%Y_%m_%d", time.localtime())+".mxd" #2015_11_24样式文件名
            newMXD=InData+"\\"+mxdName
            mxd.saveACopy(newMXD)
            del mxd
        except Exception, e:
            print "open mxd error: ", e
            return
